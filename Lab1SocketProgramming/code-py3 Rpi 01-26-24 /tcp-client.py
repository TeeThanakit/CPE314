from socket import * 
import sys

MAX_BUF = 2048

SERV_IP_ADDR, SERV_PORT = '127.0.0.1', 50001

SERV_SOCK_ADDR = (SERV_IP_ADDR, SERV_PORT)
cli_sock = socket(AF_INET, SOCK_STREAM)

print('Trying ',SERV_IP_ADDR, ':', SERV_PORT, ' ...', sep='')
cli_sock.connect(SERV_SOCK_ADDR)
print('Connected ...')

#username = input('Enter your name: ')
while True:
    print ('> ', end=' ') 
    sys.stdout.flush()
    txtout = sys.stdin.readline().strip()
    cli_sock.send(txtout.encode('utf-8'))

    if txtout == 'quit':
      break

    modifiedMsg = cli_sock.recv(MAX_BUF)
    print (modifiedMsg.decode('utf-8'))

cli_sock.close()
