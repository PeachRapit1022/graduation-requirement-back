-- SQLite
SELECT main_class.name, sub_class.name, SUM(credits.credit)
FROM user_record
JOIN credits
ON user_record.時間割コード = credits.code
JOIN main_class
ON credits.main = main_class.id
JOIN sub_class
ON credits.sub = sub_class.id


GROUP BY main_class.name, sub_class.name
ORDER BY main_class.id