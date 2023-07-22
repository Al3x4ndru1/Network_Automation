

def check_host_range(ipBase,hosts)->bool:
    
    if pow(2,(32-int(ipBase.split("/")[1]))) < len(hosts):
        
        return True
    
    return False