import socket
import time
import signal


host = socket.gethostbyname(socket.gethostname())
port = 9090
print(host)
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print("[ Server Started]")


def signal_handler(signal, frame):
    global quit
    print("exiting")
    quit = True


signal.signal(signal.SIGINT, signal_handler)
while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/", end='')
        print(data.decode("utf=8"))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print('\n [ Server Stopped ]')
        quit = True

s.close()
