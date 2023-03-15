-- 코드를 입력하세요
SELECT COUNT(*) from user_info
where joined BETWEEN '2021-01-01' AND '2021-12-31' AND AGE >= 20 AND AGE <= 29;