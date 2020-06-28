import socket

host = ''
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
while True:
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(1024)
    print(data)
    conn.close()