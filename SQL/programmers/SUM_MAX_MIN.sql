-- 최댓값 구하기 (LEVEL 1)
SELECT DATETIME 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;

-- 최솟값 구하기 (LEVEL 2)
SELECT DATETIME 시간
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;

-- 동물 수 구하기 (LEVEL 2)
SELECT COUNT(*) count
FROM ANIMAL_INS;

-- 중복 제거하기 (LEVEL 2)
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;