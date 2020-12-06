from topo.routing import Routing
import yaml
import os

class Driver:
    def __init__(self):
        super().__init__()
        f_stream = open("topo.yaml", "r");
        yaml_load = yaml.load_all(f_stream)

        edge_list = next(yaml_load)
        self.port_map = next(yaml_load)

        edge_latency = list()
        edge_capacity = list()
        for d in edge_list:
            for (k,v) in d:
                edge_latency.append(v[0])
                edge_capacity.append(v[1])

        self.rout = Routing()
        self.rout.configure_route(edge_list, edge_latency, edge_capacity)

    def install_route(self, source_AS, destination_AS, source_subnet, destination_subnet, latency, bandwidth, cost_paid, flow_id):
        routes_config = dict()
        routes_config = self.rout.get_routes(source_AS, destination_AS, source_subnet, destination_subnet, latency, bandwidth, cost_paid, flow_id)
        for routes in routes_config.get(flow_id):
            fromAS = routes[0]
            toAS = routes[1]
            sdxno = routes[2]
            inport = self.port_map.get(sdxno).get(fromAS)
            outport = self.port_map.get(sdxno).get(toAS)

            os.popen("sudo ovs-ofctl add-flow sdx{sdxn} in_port={inport},actions=output:{outport} -O OpenFlow13".format(sdxn=sdxno, inport=inport, outport=outport))
            os.popen("sudo ovs-ofctl add-flow sdx{sdxn} in_port={outport},actions=output:{inport} -O OpenFlow13".format(sdxn=sdxno, inport=inport, outport=outport))


