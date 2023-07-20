from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call


class Create_Topology():
    
    def __init__(self,
                 ipBase,
                 controller_ip,
                 controller_port,
                 switches_name,
                 hosts_name) -> None:
        self.ipBase = ipBase
        self.controller_ip = controller_ip
        self.controller_port = controller_port
        self.switches_name = switches_name
        self.hosts_name = hosts_name
        pass
    
    def create_topology(self):
        
        net = Mininet( topo=None,
                    build=False,
                    ipBase=self.ipBase)
        
        c0 = net.addController(name='c0',
                      controller=RemoteController,
                      ip=self.controller_ip, # variable that I will pass in the 
                      protocol='tcp',
                      port=self.controller_port) # vatiable with the default value of 6633
        
        
        switches_list =[]
        
        for i in self.hosts_name:
            switches_list.append(net.addSwitch(i, cls=OVSKernelSwitch))
        
        