import socket

s_add = socket.socket()
host = socket.gethostname() 
port_add = 5055
s_add.bind((host, port_add))
s_add.listen(5)

while True:
  c, addr = s_add.accept()     
  data_client = c.recv(1024)  
  data_client = data_client.decode('utf-8')
  split_str = data_client.split("|")
  value1 = split_str[0]
  if len(split_str) == 2 :
    operator = split_str[1]
  else :  
    value2 = split_str[1]
    operator = split_str[2]
  if operator == "and" :
    answer = int(value1) & int(value2)
  if operator == "or" :
    answer = int(value1) | int(value2)
  if operator == "not" :
    answer = ~int(value1)  
  ans = 'The logical operation on given numbers is : ' + str(answer)  
  c.sendall(ans.encode('utf-8'))
  c.close()            
