from socket import timeout
from scapy.all import *
import subprocess as sbp

# ICMPパケットを送って，返信させてIPアドレスを特定する
def get_ipaddr(my_ipaddr):
    #自身のIPアドレスとサブネットマスクからブロードキャストアドレスを求める．
    count = 0
    my_ip = []
    for string in my_ipaddr:
        if string == '.':
            count = count + 1
            my_ip.append(string)
            if count == 3:
                break
        else:
            my_ip.append(string)
        
    print(my_ip)

# ICMPでブロードキャストを流し，返答を受け取ることで各種アドレスを特定
def broadcastaddr():
    # ICMPパケットを流して結果を1つだけ受け取る dstの後をブロードキャストアドレスにしたいところ
    packets = Ether(dst='ff:ff:ff:ff:ff:ff')/IP(dst='192.168.1.0/24')/ICMP()
    answers = srp(packets,timeout=2)
    print(answers)

# arp
def get_macaddr():
    packet = ARP()


# hostname
def get_hostname():
    packet = ip()
    
if __name__ == '__main__':
    broadcastaddr()