import sqlite3

db = sqlite3.connect('quiz.db')

cursor = db.cursor()


cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    question TEXT NOT NULL,
    a TEXT NOT NULL,
    b TEXT NOT NULL,
    c TEXT NOT NULL,
    d TEXT NOT NULL,
    right_answer TEXT NOT NULL
)
'''
)

db.commit()
def add_question(question,a,b,c,d,right_answer):
    cursor.execute('''
        INSERT INTO questions(
                question,
                a,b,c,d,
                right_answer)
                
        VALUES (?,?,?,?,?,?)
                   
    ''',(question,a,b,c,d,right_answer))
    db.commit()
# question = input('Soraw:')
# a = input('a=')
# b = input('b=')
# c = input('c=')
# d = input('d=')
# right = input('duris juwap:')

# add_question(question=question,a=a,b=b,c=c,d=d,right_answer=right)


    




def show_questions():
    cursor.execute('''
    SELECT question,a,b,c,d FROM questions
''')
    return cursor.fetchall()


