#Test script for Room 42 environment - Files present
#Gavin Jones 15/06/2018

import os, filecmp

####################

count = 0


def filer():
    Name = os.environ['USERNAME']
    spath = 'C:/Users/{}/Desktop/IT_Files/LOGS/'.format(Name)
    jpath = 'C:/Users/{}/Desktop/IT_Files-bad/LOGS/'.format(Name)


    filestore1 = []
    filestore2 = []


    for roots, dirs, files in os.walk(spath):

        for file in files:



            filestore1.append(file)


    for roots2, dirs2, files2 in os.walk(jpath):

        for file2 in files2:

            filestore2.append(file2)

    for i in filestore1:

        for j in filestore2:

            if i == j:

                filei = open(spath + i, 'r', encoding = "ISO-8859-1")
                file_cont1 = filei.read()
                filei.close()

                filej = open(jpath + j, 'r', encoding = "ISO-8859-1")
                file_cont2 = filej.read()
                filej.close()

                if file_cont1 == file_cont2:
                    global count
                    count = count+1
                    if count == len(filestore1):
                        count = 0
                        print('The files all match and are ready for simulation')
                        break
                else:
                        print('One of the files is wrong, suggest replacement')
                        count = 0
                        break



filer()
#try and except for encoding
