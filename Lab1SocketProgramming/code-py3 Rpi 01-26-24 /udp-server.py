from socket import * 
import sys

SERV_IP_ADDR, SERV_PORT = '127.0.0.1', 50001
SERV_SOCK_ADDR = (SERV_IP_ADDR, SERV_PORT)

MAX_BUF = 2048     # Size of buffer to store received bytes

serv_sock = socket(AF_INET, SOCK_DGRAM)   # Create UDP socket
serv_sock.bind(SERV_SOCK_ADDR)            # Bind socket to address
print ('UDP server started at ', SERV_IP_ADDR,":", SERV_PORT, ' ...', sep='')

while(1):
  txtin,cli_sock_addr = serv_sock.recvfrom(MAX_BUF)  # txtin stores receive text
                                                     # cli_sock_addr stores client socket address
  cli_ip, cli_port = cli_sock_addr[0], cli_sock_addr[1]

  print (cli_ip, ':', cli_port, '>', txtin.decode("utf-8")) 
  # print (f'{cli_ip}:{cli_port}> {txtin}') # Convert byte to string and print  
  if txtin != b'quit':           # Break if user types 'quit'. 
     txtout = txtin.upper()      # Change text to upper case
     serv_sock.sendto(txtout, cli_sock_addr)     # Send it back to the client
  	 
serv_sock.close()
