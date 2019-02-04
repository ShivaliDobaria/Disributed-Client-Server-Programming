
import socket
import sys
import re

while True:
    operator = input("Enter Operator: ")
    if not re.match("^[+,*,/,-]$", operator) and operator != "and" and operator != "or" and operator != "not":
        print("Enter Valid Operator.")
        continue
    else:
        break

while True:
    value_1 = input("Enter Value1: ")
    if not re.match("^\d+$", value_1):
        print("Enter Valid Number.")
        continue
    else:
        break

if operator != "not" :
    while True:
        value_2 = input("Enter Value2: ")
        if not re.match("^\d+$", value_2):
            print("Enter Valid Number.")
            continue
        elif operator == '/' and value_2 == "0" :
            print("Enter valid value2 for division")
        else:
            break



s = socket.socket()
s_request = socket.socket()
host = socket.gethostname() 
port = 5050                
s.connect((host, port))
s.sendall(operator.encode('utf-8'))
data = s.recv(1024) 
add_port_num = data.decode('utf-8')
print("Port number for given operator : " + add_port_num)
add_port_num = int(add_port_num)
s.close()

s_operation = socket.socket()
s_operation_request = socket.socket()
s_operation.connect((host, add_port_num))
if operator == "and" or operator == "or":
    values = str(value_1 + "|" + value_2 + "|" + operator)
elif operator == "not":    
    values = str(value_1 + "|" + operator)
else :
    values = str(value_1 + "|" + value_2)
s_operation.sendall(values.encode('utf-8'))
data = s_operation.recv(1024) 
add_port_num = data.decode('utf-8')
print(add_port_num)
s_operation.close()


s1 = socket.socket()               
s1.connect((host, port))
exit_data="exit"
s1.sendall(exit_data.encode('utf-8'))
s1.close()







