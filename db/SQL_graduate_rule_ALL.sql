-- SQLite
        SELECT main_class.name AS カテゴリ1, sub_class.name AS カテゴリ2, IFNULL (sum,0) AS 取得単位,
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

        UNION ALL

        SELECT main_class.name AS カテゴリ1, sub_class.name AS カテゴリ2, IFNULL( SUM(credits.credit),0) AS 取得単位,
        IFNULL (CASE WHEN SUM(credits.credit) >= 35 THEN 'True' ELSE 35-SUM(credits.credit) END,35) AS result
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE credits.main = 3

        UNION ALL

        SELECT main_class.name AS カテゴリ1, sub_class.name AS カテゴリ2, IFNULL (SUM(credits.credit),0) AS 取得単位,
        IFNULL (CASE WHEN SUM(credits.credit) >= 14 THEN 'True' ELSE 14-SUM(credits.credit) END,14) AS result
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE credits.main = 4
        AND (credits.sub = 1 OR credits.sub = 2)

        UNION ALL

        SELECT main_class.name AS カテゴリ1, sub_class.name AS カテゴリ2, IFNULL (SUM(credits.credit),0) AS 取得単位,
        IFNULL (CASE WHEN SUM(credits.credit) >= 46 THEN 'True' ELSE 46-SUM(credits.credit) END,46) AS result
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE credits.main = 4
        AND (credits.sub >= 3 AND credits.sub <= 8)

        UNION ALL

        SELECT main_class.name AS カテゴリ1, sub_class.name AS カテゴリ2, IFNULL(sum,0) AS 取得単位,
        IFNULL(CASE WHEN sum >= tani THEN 'True' ELSE tani-sum END,tani) AS result
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
