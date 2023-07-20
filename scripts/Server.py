from flask import request, Blueprint, Response
from .service.Random_nodes_service import random_nodes_service

server = Blueprint('controller',__name__)



@server.route('/random_nodes',methods=['GET'])
def random_nodes()->list:
    
    req =request.json
    if(req["number_of_nodes"]<2):
        return "Insuficent number of nodes"
    
    return random_nodes_service(number_of_nodes=req["number_of_nodes"])


@server.route('/random_fail_node',methods=['GET'])
def random_fail_node():
    
    if request.method=='POST':
        try:
    
            req = request.json
            req["ipBase"]
            req["controller_ip"]
            req["controller_port"]
            req["switches_name"]
            req["hosts_name"]
        except Exception as e:
            return e
            
        return 


# @server.route('')
    