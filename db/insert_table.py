import sqlite3

dbname = './db/Test.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

#rating = input('rating : ')
#grades = input('grades : ')

code = input('時間割コード : ')
credit = input('単位数 : ')
main, sub = input('カテゴリ : ').split()

cur.execute(
    #'INSERT INTO rating(rating, grades) values("{}","{}")'.format(rating, grades)
    'INSERT INTO credits(code, credit, main, sub) values("{}","{}","{}","{}")'.format(code, credit, main, sub)
    )


conn.commit()
conn.close()