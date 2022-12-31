import pandas as pd
import sqlite3

csv_file = './db/editting.csv'
dbname = './db/Test.db'

df = pd.read_csv(csv_file, header=0, index_col=0)
#print(df)

conn = sqlite3.connect(dbname)
#cur = conn.cursor()
df.rename_axis(index='id').to_sql('credits', conn,if_exists='replace', index=True, dtype={'id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})
#df.to_sql('test', conn, if_exists='replace', index=False)

#conn.commit()
conn.close()