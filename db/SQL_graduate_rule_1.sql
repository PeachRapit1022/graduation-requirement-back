-- SQLite
        SELECT main_class.name AS カテゴリ名, IFNULL( SUM(credits.credit),0) AS 取得単位,
        IFNULL (CASE WHEN SUM(credits.credit) >= 35 THEN 'True' ELSE 35-SUM(credits.credit) END,35) AS result
        FROM user_record
        JOIN credits
        ON user_record.時間割コード = credits.code
        JOIN main_class
        ON credits.main = main_class.id
        WHERE credits.main = 3
