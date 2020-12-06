class Routing:
    def __init__(self, routeflag):
        if(routeflag == ""):
            self.routingproto = "sim"
        else:
            self.routingproto = "mul"
    
    def configure_route(self, edge_list, edge_latency, edge_capacity):
        pass

    def get_routes(self, source_AS, destination_AS, source_subnet, destination_subnet, latency, bandwidth, cost_paid, flow_id):
        #sends output in format
        #flow_id: [[srcAS_x, dstAS_x, SDXNo_x], [srcAS_y, dstAS_y, SDXNo_y]]
        # 0: [[2, 1, 11], [4, 2, 33], [6, 4, 22]]
        pass
        

