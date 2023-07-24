

def check_host_range(ipBase,
                     number_of_hosts,
                     number_of_switches)->bool:
    
    if (pow(2,(32-int(ipBase.split("/")[1]))) < ( int(number_of_hosts) * int(number_of_switches))):
        return bool(False)
    
    return bool(True)