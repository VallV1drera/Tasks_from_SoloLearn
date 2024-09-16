import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
   sock.bind(('192.168.0.20', 5000))
   sock.listen()
