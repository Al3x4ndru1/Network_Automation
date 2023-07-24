from flask import request, Blueprint, Response
from .service.Create_topology.Random_nodes_service import random_nodes_service
# from .service.Create_topology.Create_topology import Create_Topology
from .service.Create_topology.Check_host_range import check_host_range
from pprint import PrettyPrinter



# pprint = PrettyPrinter(indent=1,)


server = Blueprint('controller',__name__)

# for each n we add m maximum number of hosts

@server.route('/random_nodes',methods=['GET'])
def random_nodes()->list:
    
    req = request.json
    if(req["number_of_nodes"]<2):
        return "Insuficent number of nodes"
    
    return random_nodes_service(number_of_nodes=req["number_of_nodes"],
                                number_of_hosts_per_node=req["number_of_hosts_per_node"])


@server.route('/random_fail_node',methods=['POST'])
def random_fail_node():
    
    if request.method=='POST':
        try:
    
            req = request.json
            
            print(req["ipBase"],
                                        req["controller_ip"],
                                        req["controller_port"],
                                        req["switches_name_prefix"],
                                        req["hosts_name_prefix"],
                                        req["number_of_switches"],
                                        req["number_of_hosts"])
            
            if(req["controller_port"] != "default"):

                
                if (check_host_range(req["ipBase"],
                                     req["number_of_hosts"],
                                     req["number_of_switches"])):
                    topology = Create_Topology(req["ipBase"],
                                            req["controller_ip"],
                                            req["controller_port"],
                                            req["switches_name_prefix"],
                                            req["hosts_name_prefix"],
                                            req["number_of_switches"],
                                            req["number_of_hosts"])
                    topology.create_topology()
                    
                    print(req["ipBase"],
                                            req["controller_ip"],
                                            req["controller_port"],
                                            req["switches_name_prefix"],
                                            req["hosts_name_prefix"],
                                            req["number_of_switches"],
                                            req["number_of_hosts"])
                else:
                    return "Too many hosts the specified base Ip"
            else:
                
                if (req["ipBase"],req["hosts_name"]):
                    topology = Create_Topology(req["ipBase"],
                                            req["controller_ip"],
                                            6633,
                                            req["switches_name_prefix"],
                                            req["hosts_name_prefix"],
                                            req["number_of_switches"],
                                            req["number_of_hosts"])
                    topology.create_topology()
                else:
                    return "Too many hosts the specified base Ip"
                
        except Exception as e:
            return e
            
        return "Topology created"


# @server.route('/random_link_drop')
# def random_link_drop():
    
    
#     return
    