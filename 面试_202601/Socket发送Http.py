import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))

http = b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n"
s.send(http)
buffer = s.recv(1024)
print(buffer.decode('utf-8'))
s.close()
