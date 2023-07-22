from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from .Random_nodes_service import random_nodes_service

class Create_Topology():
    
        
    
    def __init__(self,
                 ipBase,
                 controller_ip,
                 controller_port,
                 switches_name_prefix,
                 hosts_name_prefix,
                 number_of_switches,
                 number_of_hosts) -> None:
        self.ipBase = ipBase
        self.controller_ip = controller_ip
        self.controller_port = controller_port
        self.switches_name_prefix = switches_name_prefix
        self.hosts_name_prefix = hosts_name_prefix
        self.number_of_switches = number_of_switches
        self.number_of_hosts = number_of_hosts
        self.copy_ipBase = ipBase
        
        
        
    def get_host(self)->str:

        ip = self.copy_ipBase.split('/')[0]

        
        a = ip.split('.')
        
        
        if 254 < (int(a[3]) + 1):
            if 254 < (int(a[2])+1):
                c = int(a[2]) +1
                host_ip = ""
                for b in range(0,1):
                    host_ip += a[b]+"."
                    
                host_ip += str(c) + "." + "0"+"."+"1"
                
                self.copy_ipBase = host_ip
                
                return host_ip
                
                
            else:
                c = int(a[2]) +1
                host_ip = ""
                for b in range(0,2):
                    host_ip += a[b]+"."
                    
                host_ip += str(c) + "." + "1"
                
                self.copy_ipBase = host_ip
                
                return host_ip
            
            

    
        c = int(a[3]) +1
        host_ip = ""
        for b in range(0,3):
            host_ip += a[b]+"."
            
        host_ip += str(c)
        
        self.copy_ipBase = host_ip
        
        return host_ip
        
        
            
    def create_topology(self):
        
        net = Mininet( topo=None,
                    build=False,
                    ipBase=self.ipBase)
        
        c0 = net.addController(name='c0',
                      controller=RemoteController,
                      ip=self.controller_ip, # variable that I will pass in the 
                      protocol='tcp',
                      port=self.controller_port) # vatiable with the default value of 6633
        
        
        switches_list = []
        
        for i in range(0,self.number_of_hosts):
            switches_list.append(net.addSwitch((self.switches_name_prefix+i), 
                                               cls=OVSKernelSwitch))
        
        
        hosts_list = []
        
        
        links = random_nodes_service(self.number_of_switches,
                                     self.number_of_hosts)
        
        
        
        
        for i in range(0,len(links)):
            
            for j in range(0,links[i]["number_of_hosts"]):
                hosts_list.append(
                    net.addHost(self.hosts_name_prefix+j, 
                            cls=Host,
                            ip= gext_host(),
                            defaultRoute=None))
                net.addLink(switches_list[i],hosts_list[j])
            
            for j in links[i]["switches_links"]:
                if(j>i):
                    net.addLink(switches_list[i],switches_list[j])
        
        
        info( '*** Starting network\n')
        net.build()
        info( '*** Starting controllers\n')
        for controller in net.controllers:
            controller.start()

        info( '*** Starting switches\n')
        for i in range(0,self.number_of_hosts):
            net.get(self.switches_name_prefix+i).start([c0])

        info( '*** Post configure switches and hosts\n')

        CLI(net)
        net.stop()