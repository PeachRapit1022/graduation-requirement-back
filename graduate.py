from pydantic import BaseModel
from typing import Union
import sqlite3
import re
import simplejson

import pandas as pd

dbname = './db/Test.db'

# 非専門科目(一般教養)
def graduate_rule_0():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT sub_class.name AS category, IFNULL (sum,0) AS sum,
        IFNULL (CASE WHEN sum >= tani THEN 0 ELSE tani-sum END, tani) AS result
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
    return df
    
# 必修科目35単位以上
def graduate_rule_1():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT main_class.name AS category, IFNULL (SUM(credits.credit), 0) AS sum,
        IFNULL (CASE WHEN SUM(credits.credit) >= 35 THEN 0 ELSE 35-SUM(credits.credit) END,35) AS result
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        WHERE credits.main = 3
        '''
    , conn)
    conn.close()
    return df

# 共通専門基礎科目or専門基礎科目の選択必修科目から14単位以上
def graduate_rule_2():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT main_class.name AS category, IFNULL (SUM(credits.credit), 0) AS sum,
        IFNULL (CASE WHEN SUM(credits.credit) >= 14 THEN 0 ELSE 14-SUM(credits.credit) END,14) AS result
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
    return df

# 市民工専門科目の選択必修科目から46単位以上
def graduate_rule_3():
    conn = sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT main_class.name AS category, IFNULL (SUM(credits.credit), 0) AS sum,
        IFNULL (CASE WHEN SUM(credits.credit) >= 46 THEN 0 ELSE 46-SUM(credits.credit) END,46) AS result
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
    return df

# 市民工各分野の選択必修科目
def graduate_rule_4():
    conn =sqlite3.connect(dbname)

    df = pd.read_sql_query(
        '''
        SELECT sub_class.name AS category, IFNULL(sum,0) AS sum,
        IFNULL(CASE WHEN sum >= tani THEN 0 ELSE tani-sum END,tani) AS result
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
    return df

def check_graduate_rule():
    df0 = graduate_rule_0().to_dict(orient='records')
    df1 = graduate_rule_1().to_dict(orient='records')
    df2 = graduate_rule_2().to_dict(orient='records')
    df3 = graduate_rule_3().to_dict(orient='records')
    df4 = graduate_rule_4().to_dict(orient='records')

    rule = [
        '1. 一般教養',
        '2. 必修科目35単位以上',
        '3. 共通専門基礎科目or専門基礎科目の選択必修科目から14単位以上',
        '4. 市民工専門科目の選択必修科目から46単位以上',
        '5. 市民工各分野の選択必修科目'
    ]

    result = [
        {'result':df0, 'rule':rule[0]},
        {'result':df1, 'rule':rule[1]}, 
        {'result':df2, 'rule':rule[2]}, 
        {'result':df3, 'rule':rule[3]},
        {'result':df4, 'rule':rule[4]}
    ]

    return result

if __name__ == '__main__':
    check_graduate_rule()