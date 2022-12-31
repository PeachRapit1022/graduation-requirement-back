import sqlite3

dbname = './db/Test.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

script = input()

cur.execute(script)

conn.commit()
conn.close()

# 削除
# DROP TABLE credits

# 新規作成
# CREATE TABLE credits(id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT, credit NUMERIC, main NUMERIC, sub NUMERIC)
