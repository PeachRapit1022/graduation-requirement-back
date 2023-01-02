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
        SELECT sub_class.name AS カテゴリ名, sum AS 取得単位,
        CASE WHEN sum >= tani THEN 'True' ELSE tani-sum END AS rerere
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
    conn.close()

    print(df)
    
# 必修科目35単位以上
def graduate_rule_1():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT main_class.name AS カテゴリ名, SUM(credits.credit) AS 取得単位,
        CASE WHEN SUM(credits.credit) >= 35 THEN 'True' ELSE 35-SUM(credits.credit) END AS rerere
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        WHERE credits.main = 3
        '''
    , conn)
    conn.close()

    #df['必要単位'] = 35
    #df['result'] = df['必要単位'] - df['取得単位']
    print(df)

# 共通専門基礎科目or専門基礎科目の選択必修科目から14単位以上
def graduate_rule_2():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT sub_class.name AS カテゴリ名, SUM(credits.credit) AS 取得単位,
        CASE WHEN SUM(credits.credit) >= 14 THEN 'True' ELSE 14-SUM(credits.credit) END AS rerere
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
    conn.close()

    #df['必要単位'] = 14
    #df['result'] = df['必要単位'] - df['取得単位']
    print(df)

# 市民工専門科目の選択必修科目から46単位以上
def graduate_rule_3():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT sub_class.name AS カテゴリ名, SUM(credits.credit) AS 取得単位,
        CASE WHEN SUM(credits.credit) >= 46 THEN 'True' ELSE 46-SUM(credits.credit) END AS rerere
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
    conn.close()
    print(df)

# 市民工各分野の選択必修科目
def graduate_rule_4():
    conn =sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT sub_class.name AS カテゴリ名, sum AS 取得単位,
        CASE WHEN sum >= tani THEN 'True' ELSE tani-sum END AS rerere
        FROM graduate_rule_4
        LEFT JOIN (

            SELECT credits.main AS main1, credits.sub AS sub1, SUM(credits.credit) AS sum
            FROM user_record
            JOIN credits
            ON user_record.時間割コード = credits.code

            GROUP BY main, sub
            ORDER BY main

        )
        ON graduate_rule_4.main = main1
        AND graduate_rule_4.sub = sub1

        LEFT JOIN main_class
        ON main = main_class.id
        LEFT JOIN sub_class
        ON sub = sub_class.id
        '''
    , conn)
    print(df)
    conn.close()

if __name__ == '__main__':
    graduate_rule_0()
    graduate_rule_1()
    graduate_rule_2()
    graduate_rule_3()
    graduate_rule_4()