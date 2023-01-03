-- SQLite
        SELECT sub_class.name AS category, IFNULL (sum,0) AS sum,
        IFNULL (CASE WHEN sum >= tani THEN 0 ELSE tani-sum END, tani) AS result
        FROM next_grade_rule
        LEFT JOIN (

            SELECT credits.main AS main1, credits.sub AS sub1, SUM(credits.credit) AS sum
            FROM user_record
            JOIN credits
            ON user_record.時間割コード = credits.code
            WHERE 評語 in ('秀','優','良','可','合格')

            GROUP BY sub
            ORDER BY main

        )
        ON next_grade_rule.main = main1
        AND next_grade_rule.sub = sub1

        LEFT JOIN main_class
        ON main = main_class.id
        LEFT JOIN sub_class
        ON sub = sub_class.id

        UNION ALL

        SELECT main_class.name AS category, IFNULL( SUM(credits.credit),0) AS 取得単位,
        IFNULL (CASE WHEN SUM(credits.credit) >= 23 THEN 0 ELSE 23-SUM(credits.credit) END,35) AS result
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE 評語 in ('秀','優','良','可','合格')
        AND credits.main = 3

        UNION ALL

        SELECT main_class.name AS category, IFNULL( SUM(credits.credit),0) AS 取得単位,
        IFNULL (CASE WHEN SUM(credits.credit) >= 54 THEN 0 ELSE 54-SUM(credits.credit) END,35) AS result
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        JOIN sub_class
        ON credits.sub = sub_class.id
        WHERE 評語 in ('秀','優','良','可','合格')
        AND credits.main = 4