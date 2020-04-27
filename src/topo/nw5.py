from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Intf

H11 = 'h51'
H11_IP = '152.168.10.11/24'
H12 = 'h52'
H12_IP = '152.168.10.12/24'
H13 = 'h53'
H13_IP = '152.168.10.13/24'
H14 = 'h54'
H14_IP = '152.168.10.14/24'
LG = '152.168.10.1'
RG = '152.168.10.1'

S11 = 's51'
S12 = 's52'
S13 = 's53'
BR1 = 'br5'
S11_DPID = '00:00:00:00:00:00:00:51'
S12_DPID = '00:00:00:00:00:00:00:52'
S13_DPID = '00:00:00:00:00:00:00:53'
BR1_DPID = '00:00:00:00:00:00:55:00'

AS_C = 'asc5'
AS_C_PORT = 6645

def as_topo():

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    as_controller = net.addController(AS_C, controller=RemoteController, ip='127.0.0.1', port=AS_C_PORT)

    h11 = net.addHost(H11, ip=H11_IP)
    h12 = net.addHost(H12, ip=H12_IP)
    h13 = net.addHost(H13, ip=H13_IP)
    h14 = net.addHost(H14, ip=H14_IP)

    s11 = net.addSwitch(S11, dpid=S11_DPID)
    s12 = net.addSwitch(S12, dpid=S12_DPID)
    s13 = net.addSwitch(S13, dpid=S13_DPID)
    br1 = net.addSwitch(BR1, dpid=BR1_DPID)

    s11.linkTo(s12)
    s11.linkTo(s13)
    s12.linkTo(h11)
    s12.linkTo(h12)
    s13.linkTo(h13)
    s13.linkTo(h14)
    s11.linkTo(br1)


    net.build()
    as_controller.start()
    s11.start([as_controller])
    s12.start([as_controller])
    s13.start([as_controller])
    br1.start([as_controller])

    net.start()
    s11.cmd('ovs-vsctl set Bridge {s11} protocols=OpenFlow13'.format(s11=S11))
    s12.cmd('ovs-vsctl set Bridge {s12} protocols=OpenFlow13'.format(s12=S12))
    s13.cmd('ovs-vsctl set Bridge {s13} protocols=OpenFlow13'.format(s13=S13))
    br1.cmd('ovs-vsctl set Bridge {br1} protocols=OpenFlow13'.format(br1=S13))

    h11.cmd('ip route add default via {LG}'.format(LG=LG))
    h12.cmd('ip route add default via {LG}'.format(LG=LG))
    h13.cmd('ip route add default via {RG}'.format(RG=RG))
    h14.cmd('ip route add default via {RG}'.format(RG=RG))
    
    
    CLI(net)
    net.stop()

if __name__ == "__main__":
    setLogLevel('info')
    as_topo()
