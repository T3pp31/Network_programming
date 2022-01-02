from scapy.all import sr1, IP, TCP
import time

ip = str(input("接続先IPを入力:"))
port = int(input('最初のポート番号を入力:'))
port_end = int(input("終端ポートを指定:"))

while port_end < port:
	print('最初と最後の数値が変')
	port = int(input('最初のポート番号を入力:'))
	port_end = int(input("終端ポートを指定:"))

open_port = []

ip = IP(dst=ip)

#syn+ackが帰って来ればポートが空いてる
#rst+ackが帰ってきたらポートは閉じている
#ステルススキャン

while port <= port_end:
	try:


		tcp = TCP(dport=port, flags='S')
		ret = sr1(ip/tcp, timeout=1, verbose=0)
		print("portnumber:{}",port)
		print('snd:{0:#010b}({1})'.format(bytes(tcp)[13],tcp.flags))
		print('rtn:{0:#010b}({1})'.format(bytes(ret['TCP'])[13],ret['TCP'].flags))

		open_flag = bytes(ret['TCP'])[13],ret['TCP'].flags
		
		if open_flag == '(20, <Flag 20 (RA)>)':
			time.sleep(5)
			open_port.append(port)
			continue
		else:
			continue

	except Exception as e:
		print("Exception:{0}".format(e))

	port = port+1

print(open_port)