import socket

"""
Here considering one of the machine as server then other two are considered to be clients
Considering one node at a time is broadcasting
Considering hardcoded IP's for stations A, B, C
 """

def sock_bind(Host, Port, num):

    s.bind((Host, Port))

    s.listen(2)
    print("Waiting for connections")

    while True:
        c, address = s.accept()

        print("Connected with", address)

        c.send(bytes(num, 'utf-8'))

        c.close


def BroadcastA(Host):
    global numsA
    numsA = []
    num = input("Enter the value of Integer")
    numsA.append(int(num))
    print(numsA)

    Port = 9999 #considering a port that is empty

    sock_bind(Host, Port, num)

def BroadcastB(Host):
    global numsB
    numsB = []
    num = input("Enter the value of Integer")
    numsB.append(int(num))

    Port = 9999 #considering a port that is empty

    sock_bind(Host, Port, num)

def BroadcastC(Host):
    global numsC
    numsC = []
    num = input("Enter the value of Integer")
    numsC.append(int(num))

    Port = 9999 #considering a port that is empty

    sock_bind(Host, Port, num)

def RecvA(localhost):

    c = socket.socket()

    c.connect(('localhost', 9999))
    x = c.recv(1024).decode()
    numsA.append(int(x))

def RecvB(localhost):
    c = socket.socket()

    c.connect(('localhost', 9999))
    x = c.recv(1024).decode()
    numsB.append(int(x))

def RecvC(localhost):
    c = socket.socket()

    c.connect(('localhost', 9999))
    x = c.recv(1024).decode()
    numsC.append(int(x))



if __name__=="__main__":

    nums = []

    s = socket.socket()
    print("Socket Created")

    # considering the hardcoded Ip for all the work stations

    Ip_A = '192.168.1.142'
    Ip_B = '192.168.1.143'
    Ip_C = '192.168.1.144'

    # Getting Ip of machine in which code is running

    localhost = socket.gethostbyname(socket.gethostname())
    print("My Ip address is", localhost)

    if (localhost == Ip_A):
        BroadcastA(localhost)
        RecvB(localhost)
        RecvC(localhost)
        print(numsA)

    elif (localhost == Ip_B):
        RecvA(localhost)
        BroadcastB(localhost)
        RecvC(localhost)
        print(numsB)

    elif (localhost == Ip_C):
        BroadcastC(localhost)
        RecvB(localhost)
        RecvA(localhost)
        print(numsC)

    else:
        pass
