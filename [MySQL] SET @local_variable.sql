SET @HOUR = -1;
SELECT (@HOUR := @HOUR + 1) AS HOUR,
    (SELECT COUNT(HOUR(DATETIME))  -- TO_NUMBER(TO_CHAR(DATETIME, 'HH24'))
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;

### SET @local_variable command로 HOUR를 -1로 정의하고, 1씩 더해서 HOUR에 할당함 (0~23까지 만들어짐)
### SubQuery를 사용해 주어진 데이터의 DATETIME HOUR과 새로 정의한 @HOUR가 같을 때 COUNT를 해줌
 
