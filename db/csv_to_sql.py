import pandas as pd
import sqlite3

csv_file = './db/id,code,credit,main,sub.csv'
#csv_file = './db/sotugyo_tanni.csv'
dbname = './db/Test.db'
table_name = 'credits'
#table_name = 'next_grade_rule'

df = pd.read_csv(csv_file, header=0, index_col=0)

conn = sqlite3.connect(dbname)
df.rename_axis(index='id').to_sql(table_name, conn,if_exists='replace', index=True, dtype={'id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})
#df.to_sql('test', conn, if_exists='replace', index=False)

conn.close()