-- SQLite
SELECT main_class.name, SUM(credits.credit) AS sum
FROM user_record
JOIN credits
ON user_record.時間割コード = credits.code
JOIN main_class
ON credits.main = main_class.id
WHERE credits.main = 3
;

