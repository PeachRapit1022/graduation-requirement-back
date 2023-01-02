-- SQLite
        SELECT sub_class.name AS カテゴリ名, IFNULL (sum,0) AS 取得単位,
        IFNULL (CASE WHEN sum >= tani THEN 'True' ELSE tani-sum END, tani) AS result
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
