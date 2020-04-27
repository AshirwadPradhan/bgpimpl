from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Intf

HX1 = 'hx1'
HX1_IP = '10.0.1.5/24'

SX1 = 'sx1'
SX1_DPID = '11:00:00:00:00:00:00:00'

SDX_GW = '10.0.1.1'

AS_C = 'sdx1'
AS_C_PORT = 6631

def as_topo():

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    as_controller = net.addController(AS_C, controller=RemoteController, ip='127.0.0.1', port=AS_C_PORT)

    hx1 = net.addHost(HX1, ip=HX1_IP)
    sx1 = net.addSwitch(SX1, dpid=SX1_DPID)
    
    sx1.linkTo(hx1)

    net.build()
    as_controller.start()
    sx1.start([as_controller])
    
    net.start()
    sx1.cmd('ovs-vsctl set Bridge {s11} protocols=OpenFlow13'.format(s11=SX1))
    
    hx1.cmd('ip route add default via {LG}'.format(LG=SDX_GW))
    
    CLI(net)
    net.stop()

if __name__ == "__main__":
    setLogLevel('info')
    as_topo()
