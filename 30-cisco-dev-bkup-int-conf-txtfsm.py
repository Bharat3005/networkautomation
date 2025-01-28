from netmiko import ConnectHandler
from operator import itemgetter
from getpass import getpass

with open('# device_ip', 'r') as devices:
    for IP in devices:

        RTR_10 = {
            'ip': IP,
            'username': 'bharatg',
            'password': 'Nyk@@123#',
            'device_type': 'cisco_ios',
        }

        net_connect = ConnectHandler(**RTR_10)

        output = net_connect.send_command('show ip int brief', use_textfsm=True)
        print(output) ### this will print dictonary output of the all the interface ###

        name = output[1]['interface']
        status = output[1]['status']
        print('\n interface' + name + 'status is '+ status)

        if status == 'up':
            print('Interface is up finishing the script')
        else:
            config_commands= ['int eth 0/1', 'no shutdown']
            output = net_connect.send_config_set(config_commands)
            print(output)
print('finished configuration')