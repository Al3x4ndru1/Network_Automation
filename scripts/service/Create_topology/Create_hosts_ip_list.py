


def create_hosts_ip_list(ipBase,hosts_name)->list:
    
    ip = ipBase.split('/')[0]
    
    hosts_ip_list = []
    
    k=1
    
    a = ip.split('.')
    
    for i in range(0,len(hosts_name)):
        if 255 < (int(ip.split('.')[3]) + k):
            if 255 < (int(ip.split('.')[2])+1):
                
                 
                for b in a:
                    host_ip += b      
                
                hosts_ip_list.append()
                k=1
                
            else:
                hosts_ip_list.append()
                k=1
        
        hosts_ip_list.append()
        k+=1