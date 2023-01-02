-- SQLite
    SELECT sub_class.name, SUM(credits.credit) AS sum
    FROM user_record
    JOIN credits
    ON user_record.時間割コード = credits.code
    JOIN main_class
    ON credits.main = main_class.id
    JOIN sub_class
    ON credits.sub = sub_class.id
    WHERE credits.main = 4
    
    AND credits.sub >= 3 AND credits.sub <= 8
;

