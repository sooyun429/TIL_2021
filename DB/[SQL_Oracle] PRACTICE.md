## [SQL_Oracle] PRACTICE



### | [JOIN](https://goddaehee.tistory.com/62)

```sql
-- https://www.hackerrank.com/challenges/challenges/problem?h_r=next-challenge&h_v=zen

SELECT A.HACKER_ID, A.NAME, B.CHALLENGES_CREATED FROM HACKERS A, (SELECT COUNT(HACKER_ID) CHALLENGES_CREATED, HACKER_ID FROM CHALLENGES GROUP BY HACKER_ID) B
WHERE A.HACKER_ID = B.HACKER_ID
ORDER BY B.CHALLENGES_CREATED DESC, A.HACKER_ID;

-- https://www.hackerrank.com/challenges/asian-population/problem

SELECT SUM(A.POPULATION) FROM CITY A, COUNTRY B
 WHERE A.COUNTRYCODE = B.CODE
   AND B.CONTINENT = 'Asia';

-- https://www.hackerrank.com/challenges/african-cities/problem

SELECT A.NAME FROM CITY A, COUNTRY B
 WHERE A.COUNTRYCODE = B.CODE
   AND B.CONTINENT = 'Africa';
   
-- https://www.hackerrank.com/challenges/full-score/problem

SELECT TEMP.hacker_id, TEMP.name FROM (
    SELECT A.hacker_id hacker_id, A.name name, COUNT(A.name) cnt
      FROM Hackers A, Difficulty B, Challenges C, Submissions D
     WHERE A.hacker_id = D.hacker_id
       AND B.difficulty_level = C.difficulty_level
       AND C.challenge_id = D.challenge_id
       AND B.score = D.score
  GROUP BY A.hacker_id, A.name
  ORDER BY COUNT(A.name) DESC, A.hacker_id ASC
) TEMP
 WHERE TEMP.cnt >= 2;
```

### | [CASE...WHEN...](https://aljjabaegi.tistory.com/15)

```sql
-- https://www.hackerrank.com/challenges/what-type-of-triangle/problem

SELECT CASE WHEN A+B > C and (A=B and B=C and C=A) THEN 'Equilateral'
            WHEN A+B > C and (A=B or B=C or C=A) THEN 'Isosceles'
            WHEN A+B > C THEN 'Scalene'
            ELSE 'Not A Triangle'
            END RESULT
FROM TRIANGLES;
```

### | CEIL, AVG, TO_NUMBER, TO_CHAR, REPLACE

```sql
-- https://www.hackerrank.com/challenges/the-blunder/problem

SELECT CEIL(AVG(A.SALARY)-AVG(B.SALARY))
  FROM EMPLOYEES A, (
       SELECT TO_NUMBER(REPLACE(TO_CHAR(SALARY), '0', '')) SALARY
         FROM EMPLOYEES) B;

-- BEST SOLUTION
SELECT CEIL(AVG(SALARY)-AVG(REPLACE(SALARY, '0', ''))) FROM EMPLOYEES;
-- 굳이 형변환을 해주지 않아도 계산가능함
-- SUBQUERY도 사용할 필요가 없음

-- discussion wrong answer
SELECT ROUND(((SELECT AVG(SALARY) FROM EMPLOYEES) - (SELECT AVG(T_SAL) FROM (SELECT TRIM('0' FROM SALARY) AS T_SAL FROM EMPLOYEES) AS TEMP)),0) AS TOTAL_COUNT;
-- 문제에서 ROUND UP TO THE 'NEXT' INTEGER이라고 명시했기 때문에 ROUND가 아닌 CEIL 함수를 사용해야 한다.
-- TRIM 함수는 양끝, LTRIM 함수는 왼쪽, RTRIM 함수는 오른쪽에 위치한 '0'값만 제거하므로 사이에 위치한 '0'은 제거해주지 않는다. (링크참고: https://gent.tistory.com/194)
```

### | COUNT, GROUP BY, ORDER BY, DESC, ROWNUM

```SQL
-- https://www.hackerrank.com/challenges/earnings-of-employees/problem

SELECT * FROM (SELECT MONTHS*SALARY, 
                      COUNT(MONTHS*SALARY)
                 FROM EMPLOYEE
               GROUP BY MONTHS*SALARY
               ORDER BY MONTHS*SALARY DESC) MAX_SAL
 WHERE ROWNUM=1;
```

### | POWER, SQRT

```SQL
-- https://www.hackerrank.com/challenges/weather-observation-station-18/problem

-- MANHATTAN DISTANCE: The distance between two points measured along axes at right angles. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.

SELECT ROUND(MAX(LAT_N)-MIN(LAT_N)+MAX(LONG_W)-MIN(LONG_W), 4) FROM STATION;

-- https://www.hackerrank.com/challenges/weather-observation-station-19/problem

-- https://coding-factory.tistory.com/436
SELECT ROUND(SQRT(POWER(MAX(LAT_N)-MIN(LAT_N), 2) + POWER(MAX(LONG_W)-MIN(LONG_W), 2)), 4) FROM STATION;
```

### | TRUNC, AVG, JOIN, GROUP BY

```SQL
-- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

SELECT A.CONTINENT, TRUNC(AVG(B.POPULATION), 0) FROM COUNTRY A, CITY B
 WHERE A.CODE = B.COUNTRYCODE
GROUP BY A.CONTINENT;
```

### | CASE...WHEN..., BETWEEN...AND...

```SQL
-- https://www.hackerrank.com/challenges/the-report/problem

SELECT CASE WHEN B.GRADE >= 8 THEN A.NAME
            ELSE 'NULL'
        END, B.GRADE, A.MARKS FROM STUDENTS A, GRADES B
 WHERE A.MARKS BETWEEN B.MIN_MARK AND B.MAX_MARK
ORDER BY B.GRADE DESC, A.NAME ASC;
```

### | JOIN, GROUP BY

```SQL
-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

SELECT A.id, B.age, A.coins_needed, A.power
  FROM WANDS A, WANDS_PROPERTY B
 WHERE A.code = B.code
   AND B.is_evil = 0
   AND A.coins_needed = (
       SELECT E.min_coins_needed
         FROM (SELECT MIN(C.coins_needed) min_coins_needed, 
                      C.power power, 
                      D.age age
                 FROM WANDS C, WANDS_PROPERTY D
                WHERE C.code = D.code
             GROUP BY C.power, D.age) E
        WHERE E.power = A.power
          AND E.age = B.age)
ORDER BY A.power DESC, B.age DESC, A.coins_needed;
```



