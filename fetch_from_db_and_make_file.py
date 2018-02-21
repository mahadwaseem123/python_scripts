"""
dsn = r'192.168.101.84'
user = r'predatarapp'
password = r'predatarapp'
database = r'PredatarV2'

con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
cnxn = pyodbc.connect(con_string)
"""

import pymssql
host = '192.168.101.84'
username = 'predatarapp'
password = 'predatarapp'
database = 'PredatarV2'


#FILEPATH = '/usr/local/lib/python2.7/dist-packages/chatterbot_corpus/data/english/tickets.yml'
FILEPATH = '/home/mahad/.local/lib/python2.7/site-packages/chatterbot_corpus/data/english/tickets.yml'


def connect_to_db():
    conn = pymssql.connect(host, username, password, database)
    cursor = conn.cursor()
    cursor.execute("SELECT question FROM Inc_Article")

    list_of_questions = []
    for row in cursor.fetchall():
        if row[0]:
            list_of_questions.append(row[0])
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM Inc_Article")
    list_of_answer = []
    for row in cursor.fetchall():
        if row[0]:
            list_of_answer.append(row[0])
    return list_of_answer, list_of_questions


def fetch_articles_from_db_and_make_file():
    list_of_answers, list_of_questions = connect_to_db()

    # list_of_questions = ['hi', 'hello', 'what is your name?']
    # list_of_answers = ['hi', 'hii', 'mahad']

    f = open(FILEPATH, "w+")
    f.write('categories:'+'\n')
    f.write('- tickets'+'\n\n')
    f.write('conversations:'+'\n')
    for ques in range(len(list_of_questions)):
        f.write('- - '+list_of_questions[ques]+'\n')
        f.write('  - '+list_of_answers[ques]+'\n\n')
    f.close()


fetch_articles_from_db_and_make_file()
