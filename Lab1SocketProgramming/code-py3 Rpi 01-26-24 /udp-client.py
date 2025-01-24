from socket import * 
import sys

MAX_BUF = 2048
SERV_IP_ADDR, SERV_PORT = '127.0.0.1', 50001

SERV_SOCK_ADDR = (SERV_IP_ADDR, SERV_PORT)     # Server socket address 
cli_sock = socket(AF_INET, SOCK_DGRAM)        # Create UDP socket
print('Server socket address: ', SERV_IP_ADDR, ':', SERV_PORT, ' ...', sep='')

while(1):
    print('> ', end='')    # Print the prompt
    sys.stdout.flush()
    txtout =  sys.stdin.readline().strip() # Take input from user keyboard
    cli_sock.sendto(txtout.encode('utf-8'), SERV_SOCK_ADDR) # Convert to byte type and send
    if txtout == 'quit':                  # Exit if user types quit
      break
    
    modifiedMsg, _ = cli_sock.recvfrom(MAX_BUF) # Wait for modified text from the server
    print (modifiedMsg.decode('utf-8'))     # Print the modified text.

cli_sock.close()
