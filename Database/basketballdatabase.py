import sqlite3

while True:
    Password = input('Please enter your password')
    try:
        if Password == 'NbaStar23':
            print('correct password')
            break
    except ValueError:
        print('incorrect password')

DATABASE = 'Basketball.db'


querytype = input('what do you want to look for: ')
if querytype == 'Everything':
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = "SELECT * from Players;"
    cursor.execute(query)
    result = cursor.fetchall()
    #print the information nicely formated
    for q in result:
        print(q)
    # close the Data base
    db.close()
