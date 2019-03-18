import sys
import os

os.chdir('/home/gavin/Desktop/Test')

def Append():
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext != '.ddd':
            os.rename(f, f + '.ddd')
    for f in os.listdir():
        print(f)
        
def Remove():
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext == '.ddd':
            os.rename(f, f_name)
    for f in os.listdir():
        print(f)


            
