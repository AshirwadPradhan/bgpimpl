topoas1:
	sudo gnome-terminal -e "python nw1.py"

topoas2:
	sudo gnome-terminal -e "python nw2.py"

topoas3:
	sudo gnome-terminal -e "python nw3.py"

topoas4:
	sudo gnome-terminal -e "python nw4.py"

topoas5:
	sudo gnome-terminal -e "python nw5.py"

topoas6:
	sudo gnome-terminal -e "python nw6.py"

topoas7:
	sudo gnome-terminal -e "python nw7.py"

topoas8:
	sudo gnome-terminal -e "python nw8.py"

toposdx1:
	sudo gnome-terminal -e "python sdx1.py"

toposdx2:
	sudo gnome-terminal -e "python sdx2.py"

toposdx3:
	sudo gnome-terminal -e "python sdx3.py"

topo: topoas1 topoas2 topoas3 topoas4 topoas5 topoas6 topoas7 topoas8 toposdx1 toposdx2 toposdx3

topo-test: topoas1 topoas2 topoas8 topoas3 topoas7 toposdx1 toposdx2

as1:
	sudo ifconfig br1 112.168.10.1/24 up
	sudo ovs-ofctl add-flow br1 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br1 action=NORMAL -O OpenFlow13
	# sudo ovs-ofctl add-flow br1 in_port=LOCAL,actions=output:1 -O OpenFlow13
	sudo ovs-ofctl add-flow s11 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s12 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s13 action=NORMAL -O OpenFlow13
	
as2:
	sudo ifconfig br2 122.168.10.1/24 up
	sudo ovs-ofctl add-flow br2 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br2 action=NORMAL -O OpenFlow13
	# sudo ovs-ofctl add-flow br2 in_port=LOCAL,actions=output:1 -O OpenFlow13
	sudo ovs-ofctl add-flow s21 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s22 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s23 action=NORMAL -O OpenFlow13

as8:
	sudo ifconfig br8 182.168.10.1/24 up
	sudo ovs-ofctl add-flow br8 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br8 action=NORMAL -O OpenFlow13

	sudo ovs-ofctl add-flow s81 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s82 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s83 action=NORMAL -O OpenFlow13

as3:
	sudo ifconfig br3 132.168.10.1/24 up
	sudo ovs-ofctl add-flow br3 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br3 action=NORMAL -O OpenFlow13

	sudo ovs-ofctl add-flow s31 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s32 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s33 action=NORMAL -O OpenFlow13

as7:
	sudo ifconfig br7 172.168.10.1/24 up
	sudo ovs-ofctl add-flow br7 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br7 action=NORMAL -O OpenFlow13

	sudo ovs-ofctl add-flow s71 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s72 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s73 action=NORMAL -O OpenFlow13

as6:
	sudo ifconfig br6 162.168.10.1/24 up
	sudo ovs-ofctl add-flow br6 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br6 action=NORMAL -O OpenFlow13

	sudo ovs-ofctl add-flow s61 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s62 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s63 action=NORMAL -O OpenFlow13

as4:
	sudo ifconfig br4 142.168.10.1/24 up
	sudo ovs-ofctl add-flow br4 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br4 action=NORMAL -O OpenFlow13

	sudo ovs-ofctl add-flow s41 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s42 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s43 action=NORMAL -O OpenFlow13

as5:
	# sudo ifconfig br5 152.168.10.1/24 up
	# sudo ovs-ofctl add-flow br5 in_port=1,actions=LOCAL -O OpenFlow13
	sudo ovs-ofctl add-flow br5 action=NORMAL -O OpenFlow13

	sudo ovs-ofctl add-flow s51 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s52 action=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow s53 action=NORMAL -O OpenFlow13

sdx1: 
	sudo ifconfig sx1 10.0.1.1/24 up
	sudo ovs-ofctl add-flow sx1 priority=1,in_port=LOCAL,actions=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow sx1 priority=1,action=NORMAL -O OpenFlow13

sdx2: 
	sudo ifconfig sx2 10.0.2.1/24 up
	sudo ovs-ofctl add-flow sx2 priority=1,in_port=LOCAL,actions=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow sx2 priority=1,action=NORMAL -O OpenFlow13

sdx3: 
	sudo ifconfig sx3 10.0.2.1/24 up
	sudo ovs-ofctl add-flow sx3 priority=1,in_port=LOCAL,actions=NORMAL -O OpenFlow13
	sudo ovs-ofctl add-flow sx3 priority=1,action=NORMAL -O OpenFlow13

ipf:
	sudo sysctl -w net.ipv4.ip_forward=1

route:
	@echo Setting route for AS1...
	sudo ip link add veth10 type veth peer name veth11
	sudo ip link set veth10 up
	sudo ip link set veth11 up
	sudo ovs-vsctl add-port br1 veth11
	sudo ovs-vsctl add-port sx1 veth10

	@echo Setting route for AS2...
	sudo ip link add veth20 type veth peer name veth21
	sudo ip link set veth20 up
	sudo ip link set veth21 up
	sudo ovs-vsctl add-port br2 veth21
	sudo ovs-vsctl add-port sx1 veth20
	# ---
	# sudo ip link add weth20 type veth peer name weth21
	# sudo ip link set weth20 up
	# sudo ip link set weth21 up
	# sudo ovs-vsctl add-port br2 weth21
	# sudo ovs-vsctl add-port sx2 weth20

	@echo Setting route for AS8...
	sudo ip link add veth80 type veth peer name veth81
	sudo ip link set veth80 up
	sudo ip link set veth81 up
	sudo ovs-vsctl add-port br8 veth81
	sudo ovs-vsctl add-port sx1 veth80
	# ---
	# sudo ip link add weth80 type veth peer name weth81
	# sudo ip link set weth80 up
	# sudo ip link set weth81 up
	# sudo ovs-vsctl add-port br8 weth81
	# sudo ovs-vsctl add-port sx2 weth80

	@echo Setting route for AS3...
	sudo ip link add veth30 type veth peer name veth31
	sudo ip link set veth30 up
	sudo ip link set veth31 up
	sudo ovs-vsctl add-port br3 veth31
	sudo ovs-vsctl add-port sx2 veth30

	@echo Setting route for AS7...
	sudo ip link add veth70 type veth peer name veth71
	sudo ip link set veth70 up
	sudo ip link set veth71 up
	sudo ovs-vsctl add-port br7 veth71
	sudo ovs-vsctl add-port sx2 veth70
	# ---
	# sudo ip link add weth70 type veth peer name weth71
	# sudo ip link set weth70 up
	# sudo ip link set weth71 up
	# sudo ovs-vsctl add-port br7 weth71
	# sudo ovs-vsctl add-port sx3 weth70

	@echo Setting route for AS4...
	sudo ip link add veth40 type veth peer name veth41
	sudo ip link set veth40 up
	sudo ip link set veth41 up
	sudo ovs-vsctl add-port br4 veth41
	sudo ovs-vsctl add-port sx3 veth40
	# ---
	# sudo ip link add weth40 type veth peer name weth41
	# sudo ip link set weth40 up
	# sudo ip link set weth41 up
	# sudo ovs-vsctl add-port br4 weth41
	# sudo ovs-vsctl add-port sx2 weth40

	@echo Setting route for AS6...
	sudo ip link add veth60 type veth peer name veth61
	sudo ip link set veth60 up
	sudo ip link set veth61 up
	sudo ovs-vsctl add-port br6 veth61
	sudo ovs-vsctl add-port sx3 veth60

	@echo Setting route for AS5...
	sudo ip link add veth50 type veth peer name veth51
	sudo ip link set veth50 up
	sudo ip link set veth51 up
	sudo ovs-vsctl add-port br5 veth51
	sudo ovs-vsctl add-port br6 veth50
	sudo ip link add weth50 type veth peer name weth51
	sudo ip link set weth50 up
	sudo ip link set weth51 up
	sudo ovs-vsctl add-port br5 weth51
	sudo ovs-vsctl add-port br4 weth50
	

config-test: as1 as2 as8 as3 as7 sdx1 sdx2 route ipf

config: as1 as2 as3 as4 as5 as6 as7 as8 sdx1 sdx2 sdx3 route ipf

clean:
	-sudo ovs-ofctl del-flows s11 -O OpenFlow13
	-sudo ovs-ofctl del-flows s12 -O OpenFlow13
	-sudo ovs-ofctl del-flows s13 -O OpenFlow13
	-sudo ovs-ofctl del-flows br1 -O OpenFlow13

	-sudo ovs-ofctl del-flows s21 -O OpenFlow13
	-sudo ovs-ofctl del-flows s22 -O OpenFlow13
	-sudo ovs-ofctl del-flows s23 -O OpenFlow13
	-sudo ovs-ofctl del-flows br2 -O OpenFlow13

	-sudo ovs-ofctl del-flows s81 -O OpenFlow13
	-sudo ovs-ofctl del-flows s82 -O OpenFlow13
	-sudo ovs-ofctl del-flows s83 -O OpenFlow13
	-sudo ovs-ofctl del-flows br8 -O OpenFlow13

	-sudo ovs-ofctl del-flows s31 -O OpenFlow13
	-sudo ovs-ofctl del-flows s32 -O OpenFlow13
	-sudo ovs-ofctl del-flows s33 -O OpenFlow13
	-sudo ovs-ofctl del-flows br3 -O OpenFlow13

	-sudo ovs-ofctl del-flows s71 -O OpenFlow13
	-sudo ovs-ofctl del-flows s72 -O OpenFlow13
	-sudo ovs-ofctl del-flows s73 -O OpenFlow13
	-sudo ovs-ofctl del-flows br7 -O OpenFlow13

	-sudo ovs-ofctl del-flows s41 -O OpenFlow13
	-sudo ovs-ofctl del-flows s42 -O OpenFlow13
	-sudo ovs-ofctl del-flows s43 -O OpenFlow13
	-sudo ovs-ofctl del-flows br4 -O OpenFlow13

	-sudo ovs-ofctl del-flows s61 -O OpenFlow13
	-sudo ovs-ofctl del-flows s62 -O OpenFlow13
	-sudo ovs-ofctl del-flows s63 -O OpenFlow13
	-sudo ovs-ofctl del-flows br6 -O OpenFlow13

	-sudo ovs-ofctl del-flows s51 -O OpenFlow13
	-sudo ovs-ofctl del-flows s52 -O OpenFlow13
	-sudo ovs-ofctl del-flows s53 -O OpenFlow13
	-sudo ovs-ofctl del-flows br5 -O OpenFlow13

	-sudo ip link del veth10
	-sudo ip link del veth20
	-sudo ip link del veth80
	-sudo ip link del veth30
	-sudo ip link del veth70
	-sudo ip link del veth40
	-sudo ip link del veth60
	-sudo ip link del veth50
	-sudo ip link del weth50
	-sudo ip link del weth20
	-sudo ip link del weth80
	-sudo ip link del weth70
	-sudo ip link del weth40

	-sudo mn -c