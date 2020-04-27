from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet, ipv4, arp, ipv6
from ryu.lib.packet import ether_types


class SimpleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SimpleSwitch13, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.ip_to_mac = {}

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # install table-miss flow entry
        #
        # We specify NO BUFFER to max_len of the output action due to
        # OVS bug. At this moment, if we specify a lesser number, e.g.,
        # 128, OVS will send Packet-In with invalid buffer_id and
        # truncated packet data. In that case, we cannot output packets
        # correctly.  The bug has been fixed in OVS v2.1.0.
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        if buffer_id:
            mod = parser.OFPFlowMod(datapath=datapath, buffer_id=buffer_id,
                                    priority=priority, match=match,
                                    instructions=inst)
        else:
            mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                    match=match, instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        # If you hit this you might want to increase
        # the "miss_send_length" of your switch
        if ev.msg.msg_len < ev.msg.total_len:
            self.logger.debug("packet truncated: only %s of %s bytes",
                              ev.msg.msg_len, ev.msg.total_len)
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        ethframe = pkt.get_protocol(ethernet.ethernet)

        #IGNORE LLDP packets
        if ethframe.ethertype == ether_types.ETH_TYPE_LLDP:
            return
        
        eth_dst = ethframe.dst
        eth_src = ethframe.src
        dpid = datapath.id

        self.mac_to_port.setdefault(dpid, {})
        self.ip_to_mac.setdefault(dpid, {})

        self.logger.info("Ethernet packet in %s %s %s %s", dpid, eth_src, eth_dst, in_port)

        # learn a mac address to avoid FLOOD next time.
        self.mac_to_port[dpid][eth_src] = in_port

        out_port = ofproto.OFPP_FLOOD

        if ethframe.ethertype == ether_types.ETH_TYPE_ARP:
            arppacket = pkt.get_protocol(arp.arp)
            src_ip = arppacket.src_ip
            self.ip_to_mac[dpid][src_ip] = eth_src
            self.receive_arp(datapath, arppacket, ethframe, in_port)
        elif ethframe.ethertype == ether_types.ETH_TYPE_IP:
            ippacket = pkt.get_protocol(ipv4.ipv4)
            src_ip = ippacket.src
            self.ip_to_mac[dpid][src_ip] = eth_src
            self.receive_ip(datapath, ippacket, ethframe, in_port)
        else:
            self.logger.info('Unknown Packet Received')
            self.logger.info('Drop Packet')
            return 1

        actions = [parser.OFPActionOutput(out_port)]

        # # install a flow to avoid packet_in next time
        # if out_port != ofproto.OFPP_FLOOD:
        #     match = parser.OFPMatch(in_port=in_port, eth_dst=dst, eth_src=src)
        #     # verify if we have a valid buffer_id, if yes avoid to send both
        #     # flow_mod & packet_out
        #     if msg.buffer_id != ofproto.OFP_NO_BUFFER:
        #         self.add_flow(datapath, 1, match, actions, msg.buffer_id)
        #         return
        #     else:
        #         self.add_flow(datapath, 1, match, actions)
        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                  in_port=in_port, actions=actions, data=data)
        datapath.send_msg(out)
    

    def receive_arp(self, datapath, arppacket, ethframe, in_port):
        src_ip = arppacket.src_ip
        src_mac = arppacket.src_mac
        dpid = datapath.id

        if arppacket.opcode == 1:
            operation = 'ARP Request'
            dst_ip = arppacket.dst_ip
        elif arppacket.opcode == 2:
            operation = 'ARP Reply'
        
        self.logger.debug('Rceived %s %s --> %s (port %s) (src_ip %s)',operation, ethframe.src, ethframe.dst, in_port, src_ip)

        if arppacket.opcode == 1:
            self.reply_arp(datapath, ethframe, arppacket, dst_ip, in_port)
        elif arppacket.opcode == 2:
            self.ip_to_mac[dpid][src_ip] = src_mac
            match = datapath.ofproto_parser.OFPMatch(
                
            )
            self.add_flow(datapath, 1, )

    def reply_arp(self, datapath, ethframe, arppacket, dst_ip, in_port):
        dpid = datapath.id
        src_ip = arppacket.src_ip
        src_mac = ethframe.src
        if dst_ip in self.ip_to_mac[dpid]:
            self.ip_to_mac[dpid][src_ip] = ethframe.src
            dst_mac = self.ip_to_mac[dpid][dst_ip]
            out_port = in_port
            self.send_arp(datapath, 2, src_mac, src_ip, dst_mac, dst_ip, out_port)
            self.logger.info('Send ARP reply to %s', src_ip)

    def send_arp(self, datapath, opcode, src_mac, src_ip, dst_mac, dst_ip, out_port):
        if opcode == 1:
            tmac = '00:00:00:00:00:00'
            tip = dst_ip
            operation = 'ARP Request'
        elif opcode == 2:
            tmac = dst_mac
            tip = dst_ip
            operation = 'ARP Reply'
        
        e = ethernet(dst_mac, src_mac, ether_types.ETH_TYPE_ARP)
        a = arp(1, 0x0800, 6, 4, opcode, src_mac, src_ip, tmac, tip)
        p = packet.Packet()
        p.add_protocol(e)
        p.add_protocol(a)
        p.serialize()

        actions = [datapath.ofproto_parser.OFPActionOutput(out_port, 0)]
        out = datapath.ofproto_parser.OFPPacketOut(datapath=datapath,
                                                    buffer_id = 0xffffffff,
                                                    in_port = datapath.ofproto.OFPP_CONTROLLER,
                                                    actions = actions,
                                                    data = p.data)
        datapath.send_msg(out)
        return 0