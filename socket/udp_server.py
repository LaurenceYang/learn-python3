import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'hello %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)