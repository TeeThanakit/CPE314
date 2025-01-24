from socket import * 
import sys
import os

SERV_IP_ADDR, SERV_PORT = '127.0.0.1', 50001

SERV_SOCK_ADDR = (SERV_IP_ADDR, SERV_PORT)
welcome_sckt = socket(AF_INET, SOCK_STREAM)
welcome_sckt.bind(addr)
welcome_sckt.listen(1)
print ('TCP forked server started ...')

while True:
  conn_sckt, cli_addr = welcome_sckt.accept()
  cli_ip, cli_port = str(cli_sock_addr[0]), str(cli_sock_addr[1]) 
  print ('New client connected from', cli_ip, ':', cli_port, ' ...')
 
  if os.fork() == 0: 
     while True:
       txtin = conn_sckt.recv(1024)
       print('Client>', txtin.decode("utf-8")) 
       if txtin == b'quit':
         conn_sckt.close()
         print('Disconnect client', cli_ip, ':', cli_addr, ' ...')
         break
       else:
         txtout = txtin.upper()    
         conn_sckt.send(txtout)
  else:
     conn_sckt.close()

