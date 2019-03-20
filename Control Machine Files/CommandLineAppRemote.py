#CommandLineAppRemote

import sys
import json
##from Machine1 import connect1

def UserInput():
    with open('Auth.json') as json_file:
        data = json.load(json_file)
        lenOfData = len(data)
        for x in range(lenOfData):
            print('{0}. {1}'.format(x+1, data['Machine '+str(x+1)][0]['Name']))
        options = input("Please type the name of the computer you would like to access\n")
        print(options)
##        for x in range(lenOfData):
##
##            for items in data.keys():
##                if('Machine {}'.format(options) == items):
##                    print ('Machine {}'.format(options))
##
##                    print('Options of functions to perform')
##                    print('1. Website checker \n2. File Checker \n3. File Replacement \n4. Email Check')
##                    while True:
##                        current = data['Machine '+options]
##                        function = input('What function would you like to perform?\n')
##                        if(function == '1'):
##                            task = 'website'
##                            MachineConnection(current, task)
##                        if(function == '2'):
##                            task = 'file'
##                            MachineConnection(current, task)
##                        if(function == '3'):
##                            task = 'replace'
##                            MachineConnection(current, task)
##                        if(function == '4'):
##                            task = 'email'
##                            MachineConnection(current, task)
##                        else:
##                            print('Please choose a number between 1 and 4')
##                    else:
##                        print('Please choose a valid Machine')
##                        break
##
##def MachineConnection(currentd, tasks):
##    connector = connect1(currentd, tasks)
##    text = '\n'.join([x.strip() for x in connector])
##    print(text)
##    restart()


def restart():
    again = input('Would you like to perform another task?')
    if(again.lower() == 'yes' or again.lower() == 'y'):
        UserInput()
    else:
        print('Thanks')
        exit()
UserInput()
