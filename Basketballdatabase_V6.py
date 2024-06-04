'''This code is a database explorer so that NBA scouts can find information about the players they need'''
'''written by Nathan Antoun'''
import sqlite3
DATABASE = 'Basketball.db'
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
while True:
    User = input('What user are you, are you a "Viewer" or an "Editor"')
    if User == 'Editor':
        Password = input('Please enter your password:\n')
        if Password != 'NbaStar23':
            print('incorrect password')
        elif Password == 'NbaStar23':
            print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats. There are 8 pre set querys you can use, \n"Everything" for all the informtation\n"Player ID" for the player ID\n"PlayerName" for the names of the players\n"Player Number" for the players number\n"Dunks" for the amount of the dunks that player has had\n"3points" for the how many 3pointers a player has had\n"PointsPerGame" for how many points the players has averaged\n"Championships" for how many championships the players has had\nAnd write anything else if you have a specific query you would like to run\nthen when you are done you can write "Done" to finish')
            while True:
                #Now there have been some pre set querys so you do not have to write a query yourself
                userinput = input(bcolors.UNDERLINE + 'What do you want to do:\n')
                if userinput == 'Everything':
                    query = 'Select * from Players'
                elif userinput == 'Player ID':
                    query = 'Select Player_ID from Players'
                elif userinput == 'Player Name':
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
                db.close()
    elif User == 'Viewer':
        Password = input('Please enter your password:\n')
        if Password != 'NbaStar24':
            print('incorrect password')
        elif Password == 'NbaStar24':
            print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats. There are 8 pre set querys you can use, \n"Everything" for all the informtation\n"Player ID" for the player ID\n"PlayerName" for the names of the players\n"Player Number" for the players number\n"Dunks" for the amount of the dunks that player has had\n"3points" for the how many 3pointers a player has had\n"PointsPerGame" for how many points the players has averaged\n"Championships" for how many championships the players has had\nAnd write anything else if you have a specific query you would like to run\nthen when you are done you can write "Done" to finish')
            while True:
                #Now there have been some pre set querys so you do not have to write a query yourself
                userinput = input(bcolors.UNDERLINE + 'What do you want to do:\n')
                if userinput == 'Everything':
                    query = 'Select * from Players'
                elif userinput == 'Player ID':
                    query = 'Select Player_ID from Players'
                elif userinput == 'Player Name':
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
                elif userinput == 'Team':
                    query = 'Select Player_Name, Team_ID from players Select Team_Name from Team'
                elif userinput == 'Done':
                    print('thank you for using this database made by Nathan Antoun, you will now be logged out')
                    break
                #now we have an option so if you want to use more complex querys you can wirte the yourself
                else:
                    print('you are a user you must use 8 of the preset querys. If you would like to do something else log in as an Editor')


                #this is the first query option
                db = sqlite3.connect(DATABASE)
                cursor = db.cursor()

                cursor.execute(query)
                result = cursor.fetchall()
                    #print the information nicely formated
                for tidy in result:
                    print(f" {tidy [1]: <30}{tidy [2]:<8}{tidy[3]:<6} ")   
                # close the Data base
                db.close()
    else:
        print('that is not a valid user')     