import socket
import subprocess
s=socket.socket()
s.connect(("10.0.0.230",1122))
subprocess.run(["ls"])
s.send(b"hello world")
s.close()
