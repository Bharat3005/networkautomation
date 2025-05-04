from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from paramiko.ssh_exception import SSHException
from getpass import getpass

# Prompt for username and password
username = input('Please enter your username: ')
password = getpass('Please enter your password: ')

# Open the file containing the list of IP addresses
with open('15_devices', 'r') as ip_list:
    for ip in ip_list:
        ip = ip.strip()
        print('Connecting to device:', ip)

        # Define the device parameters
        device = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': username,
            'password': password,
        }

        try:
            net_connect = ConnectHandler(**device)
        except NetmikoTimeoutException:
            print('Device not reachable:', ip)
            continue
        except NetmikoAuthenticationException:
            print('Authentication failure:', ip)
            continue
        except SSHException:
            print('Make sure SSH is enabled on the device:', ip)
            continue
        except Exception as e:
            print(f'An unexpected error occurred while connecting to {ip}: {e}')
            continue

        print('Checking interface status...')
        try:
            output = net_connect.send_command('show ip int brief', use_textfsm=True)
        except Exception as e:
            print(f'An error occurred while executing the command on {ip}: {e}')
            net_connect.disconnect()
            continue

        # Process and print the interface status
        print('\nList of interfaces which are UP:')
        status_up = [i['intf'] for i in output if i['status'] == 'up']
        for iface_up in status_up:
            print(iface_up)

        print('\nList of interfaces which are DOWN:')
        status_other = [i for i in output if i['status'] != 'up']
        for iface_other in status_other:
            print(f"{iface_other['intf']} {iface_other['status']}")

        # Close the connection
        net_connect.disconnect()
        print(f'Disconnected from {ip}\n')