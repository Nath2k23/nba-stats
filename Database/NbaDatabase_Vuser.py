'''This code is a database explorer so that NBA scouts can find information about the players they need'''
'''written by Nathan Antoun'''
import sqlite3
#first we have a password system so only people with authorised access can the Data base
#this is a list of options for what we can do to the terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#there is an option to be either and editor or a Veiwer
#Veiwers get limited access while editors get full access
User = input('Are you a "Viewer" or and "Editor"\n')
if User == 'Editor':
    while True:
            Password = input('Please enter your password:\n')
            if Password != 'NbaScout24':
                print('incorrect password')
            elif Password == 'NbaScout24':
                print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats. There are 8 pre set querys you can use, \n"Everything" for all the informtation\n"Player ID" for the player ID\n"PlayerName" for the names of the players\n"Player Number" for the players number\n"Dunks" for the amount of the dunks that player has had\n"3points" for the how many 3pointers a player has had\n"PointsPerGame" for how many points the players has averaged\n"Championships" for how many championships the players has had\nif you have any specific querys you would like to run you must write them yourself\nBeing and Editor you can write querys to add and delete information from the data base\nthen when you are done you can write "Done" to finish')
                while True:
                    DATABASE = 'Basketball.db'
                    #Now there have been some pre set querys so you do not have to write a query yourself
                    userinput = input(bcolors.UNDERLINE + 'What do you want to do:\n')
                    if userinput == 'Everything':
                        query = 'Select * from Players'
                    elif userinput == 'Player ID':
                        query = 'Select Player_ID from Players'
                    elif userinput == ' Player Name':
                        query = 'Select Player_Name from Players'
                    elif userinput == 'Player Number':
                        query = 'Select Player_Number from Players'
                    elif userinput == 'Dunks':
                        query = 'Select Dunks from Players'
                    elif userinput == '3points':
                        query = 'Select 3points from Players'
                    elif userinput == 'points per Game':
                        query = 'Select PointsPerGame from players'
                    elif userinput == 'Championships':
                        query = 'Select ChampionshipNumber from Players'
                    elif userinput == 'Done':
                        print('thank you for using this database made by Nathan Antoun, you will now be logged out')
                        break
                    #now we have an option so if you want to use more complex querys you can wirte the yourself
                    else:
                        query = input('if you would like to do something outside the pre set querys you must write it yourself:\n')


                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(query)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print( f"{tidy[0]:<2}{tidy[1]:<2}{tidy[2]:<2}{tidy[3]:<2}{tidy[4]:<2}{tidy[5]:<2}{tidy[6]:<2}{tidy[7]:<2}")
                        # close the Data base
                    db.close()


if User == 'Viewer':
    while True:
        Password = input('Please enter your password:\n')
        if Password != 'NbaStar23':
            print('incorrect password')
        elif Password == 'NbaStar23':
            print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats, Because you are a Veiwer you can only use preset querys. There are 8 pre set querys you can use, \n"Everything" for all the informtation\n"Player ID" for the player ID\n"PlayerName" for the names of the players\n"Player Number" for the players number\n"Dunks" for the amount of the dunks that player has had\n"3points" for the how many 3pointers a player has had\n"PointsPerGame" for how many points the players has averaged\n"Championships" for how many championships the players has had\nAnd write anything else if you have a specific query you would like to run\nthen when you are done you can write "Done" to finish')
            while True:
                    DATABASE = 'Basketball.db'
                    #Now there have been some pre set querys so you do not have to write a query yourself
                    
                    userinput = input(bcolors.UNDERLINE + 'What do you want to do:\n')
                    if userinput == 'Everything':
                        query = 'Select * from Players'
                    elif userinput == 'Player ID':
                        query = 'Select Player_ID from Players'
                    elif userinput == ' Player Name':
                        query = 'Select Player_Name from Players'
                    elif userinput == 'Player Number':
                        query = 'Select Player_Number from Players'
                    elif userinput == 'Dunks':
                        query = 'Select Dunks from Players'
                    elif userinput == '3points':
                        query = 'Select 3points from Players'
                    elif userinput == 'points per Game':
                        query = 'Select PointsPerGame from players'
                    elif userinput == 'Championships':
                        query = 'Select ChampionshipNumber from Players'
                    elif userinput == 'Done':
                        print('thank you for using this database made by Nathan Antoun, you will now be logged out')
                        break
                    else:
                        print('You are logged in as a veiwer, if you would like to do anything else you must log in as an editor')
                    #now we have an option so if you want to use more complex querys you can wirte the yourself
                    


                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(query)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print( f"{tidy[0]:<2}")
                        # close the Data base
                    db.close()
            


    
    
    
'''while True:
    DATABASE = 'Basketball.db'
    #Now there have been some pre set querys so you do not have to write a query yourself
    userinput = input(bcolors.UNDERLINE + 'What do you want to do:\n')
    if userinput == 'Everything':
        query = 'Select * from Players'
    elif userinput == 'Player ID':
        query = 'Select Player_ID from Players'
    elif userinput == ' Player Name':
        query = 'Select Player_Name from Players'
    elif userinput == 'Player Number':
        query = 'Select Player_Number from Players'
    elif userinput == 'Dunks':
        query = 'Select Dunks from Players'
    elif userinput == '3points':
        query = 'Select 3points from Players'
    elif userinput == 'points per Game':
        query = 'Select PointsPerGame from players'
    elif userinput == 'Championships':
        query = 'Select ChampionshipNumber from Players'
    elif userinput == 'Done':
        print('thank you for using this database made by Nathan Antoun, you will now be logged out')
        break
    #now we have an option so if you want to use more complex querys you can wirte the yourself
    else:
        query = input('if you would like to do something outside the pre set querys you must write it yourself:\n')


    #this is the first query option
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute(query)
    result = cursor.fetchall()
        #print the information nicely formated
    for tidy in result:
        print(tidy)
        # close the Data base
    db.close()'''
