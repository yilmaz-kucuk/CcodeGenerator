'''
   _____    _____          _         _____                           _             
  / ____|  / ____|        | |       / ____|                         | |            
 | |      | |     ___   __| | ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |      | |    / _ \ / _` |/ _ \ | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |____  | |___| (_) | (_| |  __/ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|  \_____\___/ \__,_|\___|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                   
Created on: 10 Oct 2022
Author: YilmazKUCUK      
Description: This file provides code for generate a C variable from Intel HEX
'''

hexFile = open("STM32F334_Application.hex")
out = open("fwFile.txt", 'w')

hexOut = []
lines = hexFile.readlines()
for i in lines:
    value = i.split(':')[1]
    cmdType = value[:2]
    if(cmdType == '10'):
        value = value[8:-3]
        while len(value):
            hexOut.append('0x'+value[:2])
            value = value[2:]
            hexOut.append(',')

s = ''.join(hexOut)
s = s[:-1]
sCommand = "{}{}{}{}{}".format("const uint8_t fwFile[", len(s), "] = {", s, "};")
out.write(sCommand)
print("{}{}".format("Progress completed! Size: ", len(s)))