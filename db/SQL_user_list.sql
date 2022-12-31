-- SQLite
SELECT 科目, code, credit, main_class.name, sub_class.name
FROM user_record
LEFT JOIN credits
ON user_record.時間割コード = credits.code
LEFT JOIN main_class
ON credits.main = main_class.id
LEFT JOIN sub_class
ON credits.sub = sub_class.id
WHERE credits.code IS NULL