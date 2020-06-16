class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        
        def checkv4(ip):
            p=ip.split('.')
            if len(p)!=4:
                return False
            for i in p:
                try:
                    v=int(i)
                    if v>255 or i[0]=='-' or str(v)!=i:
                        return False
                except:
                    return False
            return True
        
        def checkv6(ip):
            p=ip.split(':')
            print(p)
            if len(p)!=8:
                return False
            
            for j in p:
                l=len(j)
                if l>4 or l==0:
                        return False
                try:
                    v=int(j,16)
                    if j[0] == '-':
                        return False
                    
                except:
                    return False
            return True
        
        ip=IP
               
        if '.' in ip and checkv4(ip):
            return "IPv4"
        if ':' in ip and checkv6(ip):
            return "IPv6"
            
        return "Neither"