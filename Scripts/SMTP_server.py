cat << 'EOF' > smtp_server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.10.250', 25))
s.listen(1)
print('🚀 Dummy SMTP Server Listening...')
conn, addr = s.accept()
print(f'[*] Connection from {addr}')
conn.send(b'220 localhost ESMTP\r\n')
while True:
    data = conn.recv(1024)
    if not data: break
    msg = data.decode(errors='ignore')
    print(msg, end='')
    if 'DATA' in msg.upper(): conn.send(b'354 Go ahead\r\n')
    elif 'QUIT' in msg.upper(): conn.send(b'221 Bye\r\n'); break
    else: conn.send(b'250 OK\r\n')
conn.close()
EOF
