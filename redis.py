from socket import socket, AF_INET, SOCK_STREAM
def Scanredis(ip:str):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(10) 
    s.connect((ip, 6379))
    s.send('GET 1\r\n'.encode())
    data = s.recv(20)
    s.close()
    if '-NOAUTH'.encode() in data:
        pass
    else:
        print('yes',ip)
with open("ip_redis.txt",'r',encoding="utf-8") as f:
    for line in f:
        try:
            Scanredis(line.strip())
        except Exception as e:
            pass

# yes 120.194.242.52
# yes 222.89.91.196

