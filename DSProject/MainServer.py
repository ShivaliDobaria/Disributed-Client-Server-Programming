import socket
import os
import subprocess
import re

s = socket.socket()         
host = socket.gethostname() 
port = 5050               
s.bind((host, port))
s.listen(5)

while True:
   c, addr = s.accept()     
   print('Got connection from', addr)
   value_op = c.recv(1024)
   re_data = value_op.decode('utf-8')
   print(re_data)
   if re_data == '+' :
      add_port = 5051
      filename = "AddServer.py"
   elif re_data == '-' :
      add_port = 5052
      filename = "SubtractionServer.py"
   elif re_data == '*' :    
      add_port = 5053
      filename = "MulServer.py"
   elif re_data == '/' :    
      add_port = 5054
      filename = "DivisionServer.py"
   elif re_data == "and" or re_data == "or" or re_data == "not": 
      add_port = 5055
      filename = "LogicalServer.py"   
   elif re_data == 'exit' :
      filename = ""
      p.kill()
   else :
      add_port = "Something goes wrong...!!:("

   if filename != "" :
     p = subprocess.Popen(["python", filename])
   add_port = str(add_port)
   c.sendall(add_port.encode('utf-8'))
   c.close()        
