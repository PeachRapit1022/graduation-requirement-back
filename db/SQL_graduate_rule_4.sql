-- SQLite
SELECT main_class.name AS name1, sub_class.name AS name2, sum, tani
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
