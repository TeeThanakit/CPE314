
from socket import * 
from threading import Thread
import os,sys
import platform

SERV_IP_ADDR, SERV_PORT = '127.0.0.1', 50001

def handle_client(s, addr):
  while True:
     txtin = s.recv(1024)
     print(addr[0], ':', addr[1], '>', txtin.decode("utf-8"), sep='') 
     if txtin == b'quit':
        s.close()
        print('Disconnect client ', addr[0], ':', addr[1], ' ...', sep='')
        break
     else:
        txtout = txtin.upper()    
        s.send(txtout)
  
  return

def main():
 
  SERV_SOCK_ADDR = (SERV_IP_ADDR, SERV_PORT) 
  welcome_sckt = socket(AF_INET, SOCK_STREAM)
  
  if any(platform.win32_ver()):
    serv_sock.setsockopt(SOL_SOCKET, SO_EXCLUSIVEADDRUSE, 1)
  else:
    serv_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

  welcome_sckt.bind(SERV_SOCK_ADDR)
  welcome_sckt.listen(5)

  print ('TCP server started at ', SERV_IP_ADDR,":", SERV_PORT, ' ...', sep='')

  while True:
    conn_sckt, cli_addr = welcome_sckt.accept()
    cli_ip, cli_port = str(cli_addr[0]), str(cli_addr[1]) 
    print ('New client connected from', cli_ip, ':', cli_port, ' ...', sep='')
  
    try:
      Thread(target=handle_client, args=(conn_sckt, cli_addr,)).start()
    except:
      print("Cannot start thread ..")
      import traceback
      trackback.print_exc()

  welcome_sckt.close()

if __name__ == '__main__':
   try:
     main()
   except KeyboardInterrupt:
     print ('Interrupted ..')
     try:
       sys.exit(0)
     except SystemExit:
       os._exit(0)
