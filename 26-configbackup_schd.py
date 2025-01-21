from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException #Netmiko.exception module to handle exception
from netmiko.exceptions import SSHException 
import time
import datetime
import schedule #schedule to handle script schedule

def job():

    TNOW = datetime.datetime.now().replace(microsecond=0)
    IP_LIST = open('15_devices')
    for IP in IP_LIST:
        print ('\n  '+ IP.strip() + '  \n' )
        RTR = {
        'ip':   IP,
        'username': 'bharatg',
        'password': '', #device password 
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

        print ('Initiating cofig backup at ' + str(TNOW))
        output = net_connect.send_command('show run')

        SAVE_FILE = open("RTR_"+IP +'_'+ str(TNOW), 'w')
        SAVE_FILE.write(output)
        SAVE_FILE.close
        print ('Finished config backup')
schedule.every().minute.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)