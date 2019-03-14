import urllib.request, time

names =  {'alfa',
         'news',
         'leaks'}


websites = {'http://alfa.room42.lu/',
            'http://news.room42.lu/',
            'http://leaks.room42.lu/'}

yesList = {'yes', 'YES', 'y', 'Y'}
noList = {'n','N','no','NO'}

def main():

    for i in websites:

        try:

            urllib.request.urlopen(i)

        except Exception as e:

            for j in names:

                if j in i:

                    print (j,'is down.')

            continue;

        else:

            for j in names:

                if j in i:

                    print (j, "is up and running.")
##    restart()

##def restart():
##
##    finish = input("Are you happy now? y/n: ")
##
##    if finish in yesList:
##        print("Thanks")
##        time.sleep(3)
##        exit()
##    if finish in noList:
##        restartx = input("Would you like to run the code again? y/n: ")
##        if restartx in yesList:
##            main()
##        if restartx in noList:
##            print("As you do not want to continue, exiting program...")
##            time.sleep(3)
##            exit()
##
##    else:
##        print("Invalid answer, please answer with yes or no")
##        restart()
##

main()
##restart()
