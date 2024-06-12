'''This code is a database explorer so that NBA scouts can find information about the players they need'''
'''written by Nathan Antoun'''
import sqlite3
DATABASE = 'Basketball.db'
Everything = 'Select * from Players'
EverytingTeam = 'Select * from players, Team where players.Team_ID = Team.Team_ID'
EverythingChampionship = 'select * from players, Championships where players.ChampionshipNumber_ID = Championships.ChampNumber_ID'
option = '0'
option1 = '1'
option2 = '2'
option3 = '3'
option4 = '4'
option5 = '5'
option6 = '6'
option7 = '7' 
option8 = '8'
option9 = '9'
option10 = '10'
Exit = 'Done'
UserEditor = 'editor'
EditorPassword = 'NbaStar23'
UserViewer = 'viewer'
ViewerPassword = 'NbaStar24'
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
    if lowerUser == UserEditor:
        Password = input('Please enter your password:\n')
        if Password != EditorPassword:
            print('incorrect password')
        elif Password == EditorPassword:
            print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats, because you are an editor you have the ability to write your own querys instead of useing the 8 preset. ')
            while True:
                #Now there have been some pre set querys so you do not have to write a query yourself
                userinput = input('Select "0" to bring up the pre set querys\nWhat do you want to do:')
                
                if userinput == option:
                    print('"1" for all the informtation\n"2" for the player ID\n"3" for the names of the players\n"4" for the players number\n"5" for the Assists per game\n"6" for the amount of the dunks that player has had\n"7" for the how many 3pointers a player has had\n"8" for how many points the players has averaged\n"9" for how many championships the players has had\n"10" for the team and the conference\nAnd write anything else if you have a specific query you would like to run\nthen when you are done you can write "Done" to finish\n')
                elif userinput == option1:
                    query = Everything
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(query)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Team ID Player ID Player Name          Player Number Assists Per Game Dunks 3points Points Per Game Championships ID')
                    for tidy in result:
                        
                        print(bcolors.BOLD + f"{tidy[0]:<8}{tidy[1]:<10}{tidy[2]:<21}{tidy[3]:<14}{tidy[4]:<17}{tidy[5]:<6}{tidy[6]:<8}{tidy[7]:<16}{tidy[8]:<20}")      
                    # close the Data base
                    db.close()
            
                elif userinput == option2:
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Team ID')
                    for tidy in result:
                        
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[0]:<2}")
                    db.close()
                
                elif userinput == option3:
                     
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}")
                    db.close()
                elif userinput == option4:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Player Number')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[3]:<2}")
                    db.close()
                elif userinput == option5:
                                        
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Assists Per Game')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[4]:<4}")
                    db.close()
                elif userinput == option6:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Dunks')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[5]:<3}")
                    db.close()
                elif userinput == option7:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          3points')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[6]:<3}")
                    db.close()
                elif userinput == option8:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Points Per Game')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[7]:<3}")
                    db.close()
                
                elif userinput == option10:
                    query = EverytingTeam
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(EverytingTeam)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Team                 Conferenece')
                    for tidy in result:
                        print(f"{tidy[2]:<21}{tidy[10]:<21}{tidy[11]:<4}")
                elif userinput == option9:
                        #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(EverythingChampionship)
                    result = cursor.fetchall()
                    print('Player Name          Championships')
                        #print the information nicely formated
                    for tidy in result:
                        print(f"{tidy[2]:<21}{tidy[10]:<1}")
                

                elif userinput == Exit:
                    print('thank you for using this database made by Nathan Antoun, you will now be logged out')
                    break
                #now we have an option so if you want to use more complex querys you can wirte the yourself
                else:
                    try:
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
                    except:
                        print('that is not a valid query')
            break



    elif lowerUser == UserViewer:
        Password = input('Please enter your password:\n')
        if Password != ViewerPassword:
            print('incorrect password')
        elif Password == ViewerPassword:
            print(bcolors.BOLD + 'correct password, you know have access to the whole data base for NBA players stats, because you are a Viewer you can only use the 8 preset querys. ')
            while True:
                #Now there have been some pre set querys so you do not have to write a query yourself
                userinput = input('Select "0" to bring up the pre set querys\nWhat do you want to do:\n')
                if userinput == option:
                    print('"1" for all the informtation\n"2" for the player ID\n"3" for the names of the players\n"4" for the players number\n"5" for the Assists per game\n"6" for the amount of the dunks that player has had\n"7" for the how many 3pointers a player has had\n"8" for how many points the players has averaged\n"9" for how many championships the players has had\n"10" for the team and the conference\nthen when you are done you can write "Done" to finish\n')
                elif userinput == option1:
                    query = Everything
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(query)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Team ID Player ID Player Name          Player Number Assists Per Game Dunks 3points Points Per Game Championships ID')
                    for tidy in result:
                        
                        print(bcolors.BOLD + f"{tidy[0]:<8}{tidy[1]:<10}{tidy[2]:<21}{tidy[3]:<14}{tidy[4]:<17}{tidy[5]:<6}{tidy[6]:<8}{tidy[7]:<16}{tidy[8]:<20}")      
                    # close the Data base
                    db.close()
                elif userinput == option2:
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Team ID')
                    for tidy in result:
                        
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[0]:<2}")
                    db.close()
                
                elif userinput == option3:
                     
                    
                    #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}")
                    db.close()
                elif userinput == option4:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Player Number')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[3]:<2}")
                    db.close()
                elif userinput == option5:
                                        
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Assists Per Game')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[4]:<4}")
                    db.close()
                elif userinput == option6:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Dunks')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[5]:<3}")
                    db.close()
                elif userinput == option7:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          3points')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[6]:<3}")
                    db.close()
                elif userinput == option8:
                    
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(Everything)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Points Per Game')
                    for tidy in result:
                        print(bcolors.BOLD + f"{tidy[2]:<21}{tidy[7]:<3}")
                    db.close()
                
                elif userinput == option10:
                    query = EverytingTeam
                         #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(EverytingTeam)
                    result = cursor.fetchall()
                        #print the information nicely formated
                    print('Player Name          Team                 Conferenece')
                    for tidy in result:
                        print(f"{tidy[2]:<21}{tidy[10]:<21}{tidy[11]:<4}")
                elif userinput == option9:
                        #this is the first query option
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()

                    cursor.execute(EverythingChampionship)
                    result = cursor.fetchall()
                    print('Player Name          Championships')
                        #print the information nicely formated
                    for tidy in result:
                        print(f"{tidy[2]:<21}{tidy[10]:<1}")
                elif userinput == Exit:
                    print('thank you for using this database made by Nathan Antoun, you will now be logged out')
                    break
                #now we have an option so if you want to use more complex querys you can wirte the yourself
                else:
                    print('you are a user you must use 8 of the preset querys. If you would like to do something else log in as an Editor')


     
            break
    else:
        print('that is not a valid user')   