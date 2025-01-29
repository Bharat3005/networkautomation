from napalm import get_network_driver
driver = get_network_driver('ios') #naplam device driver
import getpass 

password = getpass.getpass("Enter device password: ")

device = driver(hostname='10.10.10.1', username='cisco', password=password,) #naplam driver method to declear the device params
device.open()
print("Successfully connected to the device", + 'hostname')

### load merge the configuration on the device using napalm ###
device.load_merge_candidate(config='int loopback 2\n ip address 2.2.2.2 255.255.255.255')

### compare the configuratio using naplam ###
print(device.compare_config())
if len(device.compare_config()) > 0: ### comparing config diff 
    choice = int("\n would like to commit the changes? [y/N]: ")
    if choice == 'y':
        print ("commiting the changes!")
        device.commit_config()  ### commiting the changes on the device
        ### rollback the changes from the running config ###
        choice = ("n\ Do you want to rollback the changes? [y/N]: ") 
        if choice == 'y':
            print("Rolling back to previous config")
            device.rollback() ### naplam config rollback 
device.close()
print("Closing the connection with device")    