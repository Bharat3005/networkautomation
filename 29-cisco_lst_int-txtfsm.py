from netmiko import ConnectHandler

# Device connection details
RTR_10 = {
    'ip': '192.168.122.10',
    'username': 'bharatg',
    'password': 'Nyk@@123#',
    'device_type': 'cisco_ios',
}

# Connect to the device
net_connect = ConnectHandler(**RTR_10)

# Run the command and parse the output
output = net_connect.send_command('show ip int brief', use_textfsm=True)
print(output)

# Check if output is valid
if output:
    print('\nList of interfaces which are UP:')
    for interface in output:
        if interface['status'] == 'up':
            print(f"{interface['interface']} {interface['status']}")

    print('\nList of interfaces which are DOWN:')
    for interface in output:
        if interface['status'] != 'up':
            print(f"{interface['interface']} {interface['status']}")
else:
    print("No interfaces found.")
