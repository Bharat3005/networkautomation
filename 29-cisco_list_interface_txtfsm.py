from netmiko import ConnectHandler
from operator import itemgetter

RTR_10 = {
    'ip':   '192.168.122.10',
    'username': 'bharatg',
    'password': 'Nyk@@123#',
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**RTR_10)

output = net_connect.send_command('show ip int brief', use_textfsm=True)
print(output)
print(output[3])
l = len(output)
print ('\nList of interfaces which are UP \n')
for i in range(0,l):
    if output[i]['status'] == 'up':
        print (output[i]['interface'] +' ' + output[i]['status'])

print ('\nList of interfaces which are DOWN \n')
for i in range(0,l):
    if output[i]['status'] != 'up':
        print (output[i]['interface'] +' ' + output[i]['status'])