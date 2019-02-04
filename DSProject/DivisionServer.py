import socket

s_add = socket.socket()
host = socket.gethostname() 
port_add = 5054
s_add.bind((host, port_add))
s_add.listen(5)

while True:
  c, addr = s_add.accept()     
  data_client = c.recv(1024)  
  data_client = data_client.decode('utf-8')
  split_str = data_client.split("|")
  value1 = split_str[0]
  value2 = split_str[1]
  ans = 'The division of given numbers is : ' + str(int(value1)/int(value2))
  c.sendall(ans.encode('utf-8'))
  c.close()            
