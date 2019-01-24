#!/usr/bin/python3

import getpass
from pexpect import pxssh

#Devices
devices = {'Raspberry': {'prompt': 'raspberrypi:', 'ip': '192.168.88.252'}, 
    'Openwrt': {'prompt': 'OpenWrt:', 'ip': '192.168.88.235'}}

#commands
commands = ['uname -a', 'uptime', 'ifconfig']

for device in devices.keys():

    outputFileName = device + '_info.txt'
    device_prompt = devices[device]['prompt']

    #Get the credentials 
    username = input(f'Username of {device} : ')
    password = getpass.getpass('Password: ')

    #ssh into the device
    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)

    #commands and output written to file
    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(devices[device]['prompt'])
            f.write(child.before)
    child.logout()