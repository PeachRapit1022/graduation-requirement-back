from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from typing import Union
import sqlite3
import re

import pandas as pd

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dbname = './db/Test.db'


def csv_to_df(raw_text: str):

    # 不要な文字を削除
    raw_text = re.sub('\n+|"+|\t+','',raw_text)

    # 改行ごとにリスト分割
    list_text = raw_text.split('\r')

    # Columnインデックス生成
    index = list_text[4].split(',')
    index.append('')

    # 不要な行を削除
    list_text = list_text[5:-1]

    # 行をカンマで区切りDF生成 左1列と右3列は不要なので削除
    table_text = [i.split(',') for i in list_text]
    df = pd.DataFrame(table_text, columns=index).iloc[:,1:7]
    
    return df

def df_to_db(df: pd.DataFrame):
    # DB操作
    conn = sqlite3.connect(dbname)
    #cur = conn.cursor()

    df.to_sql('user_record', conn, if_exists='replace')
    df1 = pd.read_sql_query(
        '''
        SELECT 科目, 時間割コード
        FROM user_record
        LEFT JOIN credits
        ON user_record.時間割コード = credits.code
        LEFT JOIN main_class
        ON credits.main = main_class.id
        LEFT JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE credits.code IS NULL
        '''   
        , conn)
    #conn.commit()
    df2  = pd.read_sql_query(
        '''
        SELECT 科目, code, credit, main_class.name, sub_class.name
        FROM user_record
        LEFT JOIN credits
        ON user_record.時間割コード = credits.code
        LEFT JOIN main_class
        ON credits.main = main_class.id
        LEFT JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE credits.code IS NOT NULL
        '''
    ,conn)
    conn.close()

    return df1, df2

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/files/")
async def file(file: bytes = File(...)):
    raw_text = file.decode('cp932')

    df = csv_to_df(raw_text)

    df1, df2 = df_to_db(df)
    conn = sqlite3.connect(dbname)

    #df1 = pd.read_sql_query(
    '''
    SELECT *
    FROM main_class
    '''
    #,conn)
    return df1.values.tolist(), raw_text

if __name__ == '__main__':
    uvicorn.run(app)
