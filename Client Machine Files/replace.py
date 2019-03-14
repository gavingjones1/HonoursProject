#Replace

import os, filecmp, re





filepathstore1 = []
filestore1 = []
filepathstore2 = []
filestore2 = []
count = 0



def FileReplace():

    #output.delete(0.0, END)
    Name = os.environ['USERNAME']
    spath = 'C:/Users/{}/Desktop/IT_Files/LOGS/'.format(Name)
    jpath = 'C:/Users/{}/Desktop/IT_Files-bad/LOGS/'.format(Name)

    for roots, dirs, files in os.walk(spath):
        
        for file in files:
            
            #output.insert(END, 'File = %s' % file + '\n')

            #filepathstore1.append(os.path.join(roots,file))
            filestore1.append(file)

            #output.insert(END, filestore1)

    for roots2, dirs2, files2 in os.walk(jpath):
        
        for file2 in files2:
            
            #output.insert(END, 'File2 = %s' % file2 + '\n')

            #filepathstore2.append(os.path.join(roots2,file2))
            filestore2.append(file2)
            #output.insert(END, filestore2)
            




    
    for i in filestore1:

        for j in filestore2:

            if i == j:
                #shutil
                with open(spath + i, encoding = "ISO-8859-1") as f:
                    with open(jpath + j, "w", encoding = "ISO-8859-1") as f1:
                        for line in f:
                            f1.write(line)
    print('Files replaced')

FileReplace()
