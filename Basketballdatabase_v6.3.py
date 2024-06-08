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
    lowerUser = User.lower()
    if lowerUser == 'editor':
        Password = input('Please enter your password:\n')
        if Password != 'NbaStar23':
            print('incorrect password')
        elif Password == 'NbaStar23':
            print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats, because you are an editor you have the ability to write your own querys instead of useing the 8 preset. ')
            while True:
                #Now there have been some pre set querys so you do not have to write a query yourself
                userinput = input('Select "0" to bring up the pre set querys\nWhat do you want to do:')
                
                if userinput == '0':
                    print('"1" for all the informtation\n"2" for the player ID\n"3" for the names of the players\n"4" for the players number\n"5" for the Assists per game\n"6" for the amount of the dunks that player has had\n"7" for the how many 3pointers a player has had\n"8" for how many points the players has averaged\n"9" for how many championships the players has had\n"10" for the team and the conference\nAnd write anything else if you have a specific query you would like to run\nthen when you are done you can write "Done" to finish\n')
                elif userinput == '1':
                    query = 'Select * from Players'
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(query)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[0]:<3}{tidy[1]:<3}{tidy[2]:<21}{tidy[3]:<5}{tidy[4]:<5}{tidy[5]:<3}{tidy[6]:<5}{tidy[7]:<5}{tidy[8]:<5}")      
                    # close the Data base
                    db.close()
            
                elif userinput == '2':
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[0]:<2}")
                    db.close()
                
                elif userinput == '3':
                    query = 'Select Player_Name from Players'
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}")
                    db.close()
                elif userinput == '4':
                    query = 'Select Player_Number from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[3]:<2}")
                    db.close()
                elif userinput == '5':
                                        
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[4]:<4}")
                    db.close()
                elif userinput == '6':
                    query = 'Select Dunks from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[5]:<3}")
                    db.close()
                elif userinput == '7':
                    query = 'Select 3points from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[6]:<3}")
                    db.close()
                elif userinput == '8':
                    query = 'Select PointsPerGame from players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[7]:<3}")
                    db.close()
                elif userinput == '9':
                    query = 'Select ChampionshipNumber from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[8]:1}")
                    db.close()
                elif userinput == '10':
                    query = 'Select * from players, Team where players.Team_ID = Team.Team_ID'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players, Team where players.Team_ID = Team.Team_ID')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(f"{tidy[2]:<21}{tidy[10]:<21}{tidy[11]:<4}")
                elif userinput == 'Done':
                    print('thank you for using this database made by Nathan Antoun, you will now be logged out')
                    break
                #now we have an option so if you want to use more complex querys you can wirte the yourself
                else:
                    query = input('if you would like to do something outside the pre set querys you must write it yourself:\n')
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(bcolors.BOLD + query)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(tidy)   
                    # close the Data base
                    db.close()
            break



    elif lowerUser == 'viewer':
        Password = input('Please enter your password:\n')
        if Password != 'NbaStar24':
            print('incorrect password')
        elif Password == 'NbaStar24':
            print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats, because you are a Viewer you can only use the 8 preset querys. ')
            while True:
                #Now there have been some pre set querys so you do not have to write a query yourself
                userinput = input('Select "0" to bring up the pre set querys\nWhat do you want to do:')
                if userinput == '0':
                    print('"1" for all the informtation\n"2" for the player ID\n"3" for the names of the players\n"4" for the players number\n"5" for the Assists per game\n"6" for the amount of the dunks that player has had\n"7" for the how many 3pointers a player has had\n"8" for how many points the players has averaged\n"9" for how many championships the players has had\n"10" for the team and the conference\nthen when you are done you can write "Done" to finish\n')
                elif userinput == '1':
                    query = 'Select * from Players'
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(query)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[0]:<3}{tidy[1]:<3}{tidy[2]:<21}{tidy[3]:<5}{tidy[4]:<5}{tidy[5]:<3}{tidy[6]:<5}{tidy[7]:<5}{tidy[8]:<5}")      
                    # close the Data base
                    db.close()
            
                elif userinput == '2':
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[0]:<2}")
                    db.close()
                
                elif userinput == '3':
                    query = 'Select Player_Name from Players'
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}")
                    db.close()
                elif userinput == '4':
                    query = 'Select Player_Number from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[3]:<2}")
                    db.close()
                elif userinput == '5':
                                        
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[4]:<4}")
                    db.close()
                elif userinput == '6':
                    query = 'Select Dunks from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[5]:<3}")
                    db.close()
                elif userinput == '7':
                    query = 'Select 3points from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[6]:<3}")
                    db.close()
                elif userinput == '8':
                    query = 'Select PointsPerGame from players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[7]:<3}")
                    db.close()
                elif userinput == '9':
                    query = 'Select ChampionshipNumber from Players'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[8]:1}")
                    db.close()
                elif userinput == '10':
                    query = 'Select * from players, Team where players.Team_ID = Team.Team_ID'
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute('Select * from players, Team where players.Team_ID = Team.Team_ID')
                    result = cursor.fetchall()
                        #print the information nicely formated
                    for tidy in result:
                        print(f"{tidy[2]:<21}{tidy[10]:<21}{tidy[11]:<4}")
                elif userinput == 'Done':
                    print('thank you for using this database made by Nathan Antoun, you will now be logged out')
                    break
                #now we have an option so if you want to use more complex querys you can wirte the yourself
                else:
                    print('you are a user you must use 8 of the preset querys. If you would like to do something else log in as an Editor')


     
            break
    else:
        print('that is not a valid user')     

    
    
    
