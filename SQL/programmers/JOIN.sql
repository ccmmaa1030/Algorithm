-- 없어진 기록 찾기 (LEVEL 3)
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS LEFT OUTER JOIN ANIMAL_INS INS
    ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID;

-- 있었는데요 없었습니다 (LEVEL 3)
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS INS INNER JOIN ANIMAL_OUTS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME;

-- 오랜 기간 보호한 동물(1) (LEVEL 3)
SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS INS LEFT OUTER JOIN ANIMAL_OUTS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME
LIMIT 3;

-- 보호소에서 중성화한 동물 (LEVEL 4)
SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME
FROM ANIMAL_INS INS INNER JOIN ANIMAL_OUTS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE LIKE 'Intact%' 
      AND (OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%' OR OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY OUTS.ANIMAL_ID;