import socket
import random
import mysqltest
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port=random.randrange(1111,5555)
address=(ip,port)
server.bind(address)
server.listen(1)
print"started listening on",ip,":",port
client,addr=server.accept()
print"got a connection from",addr[0],":",addr[1]
while True:
    data=client.recv(1024)
    print"recieved",data,"from the client"
    print"processing data"
    if data[0:4]=='cart':
        x=[]
        x=data[5:].split(' ')
        print x
        a2=mysqltest.fetching_data()
        a2.insert(x)
        print"got back from rasberry pi"
    else:    
        a=mysqltest.fetching_data()
        b,c,d,e=a.query_with_fetchone(data)
        b=str(b)
        c=str(c)
        d=str(d)
        e=str(e)
        ans=b+" "+c+" "+d+" "+e
        if data==b:
            client.send(ans)
            print"processing done and reply sent"
        elif data=="disconnect":
            client.send("goodbye")
            client.close()
            break
        else:
            client.send("invalid data")
            print"processing done invalid and reply sent"
        

