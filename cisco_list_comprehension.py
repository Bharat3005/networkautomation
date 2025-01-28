from netmiko import ConnectHandler
from operator import itemgetter
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException #Netmiko.exception module to handle exception
from netmiko.exceptions import SSHException
from getpass import getpass

Password = getpass('Please enter device password: ')

IP_LIST = open('15_devices')
for IP in IP_LIST:
    print('connecting to device: ', IP)

    RTR_10 = {
        'ip':   IP,
        'username': 'admin',
        'password': Password,
        'device_type': 'cisco_ios',
    }
    try:
            net_connect = ConnectHandler(**RTR)
        except NetmikoTimeoutException:
            print ('Device not reachable.')
            continue
        except NetmikoAuthenticationException:
            print ('Authentication Failure.')
            continue
        except SSHException:
            print ('Make sure SSH is enabled in device.')
            continue
  

    print ('Checking interface status..')
    net_connect = ConnectHandler(**RTR_10)

    output = net_connect.send_command('show ip int brief', use_textfsm=True)


    devlist = []
    for i in output:
        if i['status'] == 'up':
            devlist.append(i['intf'])
        print(devlist)

        print([i for i in output if i['status'] == 'up'])
        print ([i['interface'] for i in output if i['status'] == 'up'])

        print('\n \n')

        print ('\nList of interfaces which are UP \n')
        statusup =[i['interface'] for i in output if i['status'] == 'up']

        for ifaceup in statusup:
            print (ifaceup)

        print ('\nList of interfaces which are DOWN \n')
        statusother =[i for i in output if i['status'] != 'up']
        for ifaceother in statusother:
            print (ifaceother['interface'] + ' ' + ifacesother['status']  )