import os, time

spath = ['./keylogger.py']

def doesFileExist(spath):
    return os.path.exists(spath)
##    if os.path.exists == True:
##        print('This file exists')
##    else:
##        print('fuck u try again')
##        timer()

def timer():
    time.sleep(5)
    for i in spath:
        
        if doesFileExist(i):
            
            print ('Yes',i, ' exists')
            
            os.system("python H:\year 4\gitrep\Honours\HonoursProject\Honours code\keylogger.py")
            
        else:
            
            print('No',i, 'does not exist')
            timer()

timer()
