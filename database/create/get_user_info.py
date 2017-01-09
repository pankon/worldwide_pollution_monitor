#!/usr/bin/env python2

def get_ip():
    # From http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    # kudos to UnkwnTech
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip = s.getsockname()[0]
    s.close()  
    return ip
    
def main():
    print(get_ip())
    
if __name__ == '__main__':
    main()
    
