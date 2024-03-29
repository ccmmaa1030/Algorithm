-- 고양이와 개는 몇 마리 있을까 (LEVEL 2)
SELECT ANIMAL_TYPE, COUNT(*) count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
HAVING ANIMAL_TYPE LIKE 'Cat%' OR ANIMAL_TYPE LIKE 'Dog%'
ORDER BY ANIMAL_TYPE;

-- 동명 동물 수 찾기 (LEVEL 2)
SELECT NAME, COUNT(*) COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(*) > 1
ORDER BY NAME;

-- 입양 시각 구하기(1) (LEVEL 2)
SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 and HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME);

-- 입양 시각 구하기(2) (LEVEL 4)
SET @h := -1;
SELECT (@h := @h+1) HOUR, 
       (SELECT COUNT(*)
        FROM ANIMAL_OUTS
        WHERE HOUR(DATETIME) = @h) COUNT
FROM ANIMAL_OUTS
WHERE @h < 23;