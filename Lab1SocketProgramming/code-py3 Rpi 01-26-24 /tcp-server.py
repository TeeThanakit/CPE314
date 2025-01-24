from socket import * 
import sys
import platform


SERV_IP_ADDR, SERV_PORT = '127.0.0.1', 50001

SERV_SOCK_ADDR = (SERV_IP_ADDR, SERV_PORT)
serv_sock = socket(AF_INET, SOCK_STREAM)

if any(platform.win32_ver()):
  serv_sock.setsockopt(SOL_SOCKET, SO_EXCLUSIVEADDRUSE, 1)
else:
  serv_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  
serv_sock.bind(SERV_SOCK_ADDR)
serv_sock.listen(1)

print ('TCP server started at ', SERV_IP_ADDR,":", SERV_PORT, ' ...', sep='')

while True:
  conn_sock, cli_sock_addr = serv_sock.accept()
  cli_ip, cli_port = str(cli_sock_addr[0]), str(cli_sock_addr[1]) 
  print ('New client connected from ', cli_ip, ':', cli_port, ' ...', sep='')

  while True:
     txtin = conn_sock.recv(1024)
     print (cli_ip, ':', cli_port, '> ', txtin.decode("utf-8"), sep='') 

     if txtin == b'quit':
       conn_sock.close()
       print('Disconnect client ', cli_ip, ':', cli_port, ' ...', sep='')
       print('Waiting for a new client ...')
       break
     else:
       txtout = txtin.upper()    
       conn_sock.send(txtout)
  
conn_sock.close()
