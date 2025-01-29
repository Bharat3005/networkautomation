from napalm import get_network_driver
import re
from getpass import getpass

version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_no_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')

driver = get_network_driver('ios') #naplam device driver

password = getpass('Enter device password: ')

device = driver(hostname='10.10.10.1', username='cisco', password=password,) #naplam driver method to declear the device params
# print(type(driver))
# print(dir(device))

### Connecting to the device ###
device.open()
print("Connected successfully with device")

show_commands = device.cli(['show ip int br', 'show version'])
print(show_commands)
print(show_commands['show ip int br'])

show_ver = show_commands['show version']

version_match = version_pattern.search(show_ver)
print('IOS Version'.ljust(18) + ': ' + version_match.group(1))

model_match = model_pattern.search(show_ver)
print('Model '.ljust(18) + ': ' + model_match.group(1))

serial_no_match = serial_no_pattern.search(show_ver)
print('Serial Number '.ljust(18) + ': ' + serial_no_match.group(1))

uptime_match = uptime_pattern.search(show_ver)
print('Host Name '.ljust(18) + ': ' + uptime_match.group(1))
print('Device Uptime '.ljust(18) + ': ' + uptime_match.group(2))

device.close()
print("Disconnected from the device")
