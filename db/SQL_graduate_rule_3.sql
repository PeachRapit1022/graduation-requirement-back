-- SQLite
        SELECT sub_class.name AS カテゴリ名, IFNULL (SUM(credits.credit),0) AS 取得単位,
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
