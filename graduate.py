from pydantic import BaseModel
from typing import Union
import sqlite3
import re

import pandas as pd

dbname = './db/Test.db'

# 非専門科目(一般教養)
def graduate_rule_0():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT main_class.name AS name1, sub_class.name AS name2, sum, tani
        FROM graduate_rule_0
        LEFT JOIN (

            SELECT credits.main AS main1, credits.sub AS sub1, SUM(credits.credit) AS sum
            FROM user_record
            JOIN credits
            ON user_record.時間割コード = credits.code

            GROUP BY main, sub
            ORDER BY main

        )
        ON graduate_rule_0.main = main1
        AND graduate_rule_0.sub = sub1

        LEFT JOIN main_class
        ON main = main_class.id
        LEFT JOIN sub_class
        ON sub = sub_class.id
        '''
    , conn)
    print(df)
    conn.close()

# 必修科目35単位以上
def graduate_rule_1():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT main_class.name, SUM(credits.credit) AS sum
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        WHERE credits.main = 3
        '''
    , conn)
    print(df)
    conn.close()

# 共通専門基礎科目or専門基礎科目の選択必修科目から14単位以上
def graduate_rule_2():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT sub_class.name, SUM(credits.credit) AS sum
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE credits.main = 4
        AND (credits.sub = 1 OR credits.sub = 2)
        '''
    , conn)
    print(df)
    conn.close()

def graduate_rule_3():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT sub_class.name, SUM(credits.credit) AS sum
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE credits.main = 4
        AND (credits.sub >= 3 AND credits.sub <= 8)
        '''
    , conn)
    print(df)
    conn.close()
