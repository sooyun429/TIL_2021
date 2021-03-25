## SQL_Oracle

### | DB작성 기본 
```sql
-- DB Object

-- 테이블 조회
select * from all_tables
where owner = 'TSTAPOWNER'
and table_name like 'MT%'

-- object 조회
select * from all_objects
where owner = 'DEVAPOWNER'
and object_type = 'FUNCTION'

-- select insert(컬럼의 갯수가 동일하지 않으면 에러 남)
insert into a (id, pwd)
select (id, pwd) from b;

--db objects vaild
select distinct name from all_source
where text like '%키워드%'

-- view 조회
select * from all_views;
```

### | 연산자 및 함수

#### [SQL 함수 유형]

- 단일 행 함수: 함수는 단일 행에서만 실행되며 행당 하나의 결과를 반환한다. 문자, 숫자, 날짜, 변환, 일반 등의 유형이 있다.
- 다중 행 함수: 행 그룹당 하나의 결과를 산출하도록 행 그룹을 조작할 수 있다. 이러한 함수를 그룹 함수라고도 하며 그룹 함수를 사용하여 집계된 데이터를 출력할 수 있다.


#### [LIKE]

- ESCAPE : 와일드 카드 문자를 일반문자 처럼 사용하고 싶은 경우에 사용
  ex) WHERE name LIKE '%a\\_y%' ESCAPE '\\'
- LIKE 연산자는 대소문자를 구분 한다.
- UPPER() 함수를 이용해 대소문자 구분없이 출력 할 수 있다.
  (인덱스 성능문제 발생, 함수기반 인덱스 사용)

#### [[DECODE](https://gent.tistory.com/227)]

- DECODE(VALUE, IF1, THEN1, IF2, THEN2...): VALUE 값이 IF1일 경우 THEN1 값을 반환하고, VALUE 값이 IF2일 경우 THEN2 값을 반환한다.
- DECODE 함수는 조건에 따라 데이터를 다른 값이나 컬럼값으로 추출할 수 있다.
- DECODE 함수 안에 DECODE 함수를 중첩으로 사용할 수 있다.

#### [[CASE-WHEN](http://www.gurubee.net/lecture/1028)]

- CASE 함수는 DECODE함수가 제공하지 못하는 비교연산의 단점을 해결할 수 있는 함수이다.
- DECODE함수에서 비교연산을 수행하기 위해서는 GREATEST, LEAST등의 함수를 사용해야 하지만, CASE함수에서는 조건 연산자를 모두 사용 할 수 있다.
- CASE함수는 IF.. THEN .. ELSE 구문과 비슷 하다. WHEN절 다음에 여러 조건이 올 수 있다.

#### [[ROUND, TRUNC, CEIL](https://coding-factory.tistory.com/295)]

#### [[OVER](https://javaexpert.tistory.com/503)]

- COUNT(*) OVER(): 전체행 카운트. OVER함수는 ORDER BY, GROUP BY 서브쿼리를 개선하기 위해 나온 함수이다. 

#### [AND/OR 연산자]
- `AND` 연산자가 `OR` 연산자에 비해 우선순위가 높다. `OR` 연산자를 먼저 수행하려면 괄호를 사용하여 실행 순서를 변경해야 한다.

#### [ORDER BY]
- SQL 문에서 ORDER BY 절을 사용하는 경우 그 뒤에 다른 절을 사용할 수 없다. 또한 표현식, alias 또는 열 위치를 정렬 조건으로 지정할 수 있다. NULLS FIRST 또는 NULLS LAST 키워드를 사용하여 반환된 행 중 null 값을 포함하는 행이 정렬 순서상 맨 처음에 나타나거나 마지막에 나타나도록 지정할 수 있다.
- NULL 값은 오름차순에서 마지막에 표시되고, 내림차순에서 처음에 표시됨

### | [NULL값 처리](http://www.gurubee.net/lecture/1880)

- NVL(column, value): 해당 컬럼이 null인 경우 입력한 value값으로 바꾸어 출력

- NVL2(column, value1, value2): 해당 컬럼 값이 null이 '아닌' 경우 value1을 반환하고, null인 경우 value2를 반환

- NULLIF(column1, column2): column1과 column2 값이 동일하면 NULL, 그렇지 않으면 column1을 반환

  - CASE WHEN column1 = column2 THEN NULL ELSE column1 END

- COALESCE(column, value1, value2, ...): 해당 컬럼이 NULL 값이 '아니면' 해당 컬럼 값을, NULL 값이면 COALESCE(value1, value2, ...) 값을 반환 (NVL 함수와 비슷하다.)

### | [DELETE(DML), DROP(DDL), TRUNCATE(DDL) 비교](http://www.gurubee.net/article/1455)

- DELETE FROM [TABLE NAME];
  - DELETE 문을 사용할 때 TABLE이나 CLUSTER에 행이 많으면 행이 삭제될 때마다 많은 SYSTEM 자원이 소모된다. 예를 들어 CPU 시간,REDO LOG 영역,  TABLE이나 INDEX에 대한 ROLLBACK SEGMENT 영역 등의 자원이 필요하다.
  - TRIGGER가 걸려있다면 각 행이 삭제될 때 실행된다.
  - 할당되었던 영역은 삭제되어 빈 TABLE이나 CLUSTER에 그대로 남아 있게 된다.
- DROP TABLE [TABLE NAME];
  - TABLE이나 CLUSTER를 삭제하고 재생성하면 모든 관련된 INDEX, CONSTRAINT, TRIGGER도 삭제되며, 삭제된 TABLE이나 CLUSTERED TABLE에 종속된 OBJECTS는 무효화 된다.
  - 삭제된 TABLE이나 CLUSTERED TABLE에 부여된 권한도 삭제된다.
- TRUNCATE TABLE [TABLE NAME];
  - TRUNCATE 명령어는 TABLE이나 CLUSTER에서 모든 행을 삭제하는 빠르고 효율적인 방법이다.
  - 어떤 ROLLBACK 정보도 만들지 않고 즉시 COMMIT한다. TRUNCATE 명령어는 DDL 명령문으로 ROLLBACK될 수 없다.
  - 잘라 버릴 TABLE과 관련된 구조(CONSTRAINT, TRIGGER 등)과 권한에 영향을 주지 않는다.  
  - TABLE에서 ROW를 삭제하면 해당 TABLE에 걸려 있는 TRIGGER는 실행되지 않는다.
  - AUDIT 기능이 ENABLE되어 있으면, TRUNCATE 명령문은 DELETE 문에 해당하는 AUDIT 정보를 생성하지 않는다. 대신 발생한 TRUNCATE 명령문에 대한 단일 AUDIT RECORD를 생성한다.

### | 데이터베이스와 데이터웨어하우스의 차이점

- 데이터베이스: 체계적인 데이터 모음로 트랜잭션 처리에 사용된다. 많은 데이터를 저장하며 자주 업데이트 되며 현재 데이터가 들어있다.
- 데이터웨어하우스: 특수한 유형의 데이터베이스로 쿼리 및 보고에 최적화되어 분석 처리에 사용된다. 데이터베이스의 변경사항을 포함하는 기록 데이터가 들어있다.


### | [정적쿼리 vs 동적쿼리](https://steemit.com/oracle/@ekkim/oracle)
- 정적쿼리
  - 고정된 SQL 형태를 만들어 사용 (일반적으로 작성된 SQL쿼리)
  - Parsing 되면 Memory에 상주하면서 Shared
    => Stored Procedure에 새로 캐싱되지 않아 재사용성 있음
- 동적쿼리
  - 입력값이나 변경 사항을 추가해 실행할 쿼리문을 문자열로 SQL 변수에 작성해 담아 만든 후 DBMS에서 콜
  - 실행될 때마다 Parsing
    => Stored Procedure를 생성할 때 새로 캐싱되어 재사용성 떨어뜨림

![정적쿼리_동적쿼리_특징](https://github.com/sooyun429/TIL_2021/blob/master/DB/images/%EC%A0%95%EC%A0%81%EC%BF%BC%EB%A6%AC_%EB%8F%99%EC%A0%81%EC%BF%BC%EB%A6%AC_%ED%8A%B9%EC%A7%95.png?raw=true)

- 참고링크:
  - [https://kslee7746.tistory.com/](https://kslee7746.tistory.com/entry/Java-MVC-정적-쿼리-동적-쿼리)
  - https://blackas119.tistory.com/38
  - https://m.blog.naver.com/PostView.nhn?blogId=leeoh04&logNo=20111395137&proxyReferer=https:%2F%2Fwww.google.com%2F


### | 서브쿼리
- WITH절

  - 특징:
    - 동일한 SQL이 반복되어 사용될 때 성능을 높이기 위해 사용된다.
    - 임시 테이블을 사용한다.
    - 별칭으로 사용한 SELECT 문의 FROM 절에 다른 SELECT 구문의 별칭 참조가 가능하다.
  - 장점:
    - 동일한 구문을 한 번만 사용할 수 있다면 쿼리가 훨씬 간단해진다.
    - 굳이 테이블을 생성하지 않고 임시 테이블을 사용해서 데이터를 엑세스하기 때문에 성능이 좋다.
  - 유의점:
    - 같은 시간에 여러 개의 WITH절을 돌리는 등 WITH절을 잘못 사용하는 경우 임시테이블이 견딜 수 있는 정도를 넘어서 다같이 처리 속도가 느려질 수 있다.
  - 일반 서브 쿼리와 WITH절

  ![SQL WITH절 설명](https://github.com/sooyun429/TIL_2021/blob/master/DB/images/SQL%20WITH%EC%A0%88%20%EC%84%A4%EB%AA%85.jpg?raw=true)

  ```sql
  --  기본 FORMAT
  WITH 별칭1 AS (서브쿼리)
     , 별칭2 AS (서브쿼리)
  ...
  SELECT ...
  FROM 별칭1, 별칭2
  ...
  ```

  ```sql
  -- 적용예시 1 (기존쿼리)
  SELECT b2.*
    FROM ( SELECT period, region, sum(loan_jan_amt) jan_amt
             FROM kor_loan_status
         GROUP BY period, region
          ) b2,
          ( SELECT b.period,  MAX(b.jan_amt) max_jan_amt
             FROM ( SELECT period, region, sum(loan_jan_amt) jan_amt
                      FROM kor_loan_status
                  GROUP BY period, region
                  ) b,
                  ( SELECT MAX(PERIOD) max_month
                      FROM kor_loan_status
                  GROUP BY SUBSTR(PERIOD, 1, 4)
                  ) a
             WHERE b.period = a.max_month
          GROUP BY b.period
          ) c
     WHERE b2.period = c.period
       AND b2.jan_amt = c.max_jan_amt
  ORDER BY 1;
  ```

  ```sql
  -- 적용예시 1 (수정쿼리)
    WITH b AS ( SELECT period, region, sum(loan_jan_amt) jan_amt
                  FROM kor_loan_status
              GROUP BY period, region
               ),
         c AS ( SELECT b.period,  MAX(b2.jan_amt) max_jan_amt
                  FROM b,
                       ( SELECT MAX(PERIOD) max_month
                           FROM kor_loan_status
                       GROUP BY SUBSTR(PERIOD, 1, 4)
                       ) a
                 WHERE b.period = a.max_month
              GROUP BY b.period
               )
    SELECT b.*
      FROM b, c
     WHERE b.period = c.period
       AND b.jan_amt = c.max_jan_amt
  ORDER BY 1;
  ```

  ```sql
  -- 적용예시 2
  WITH bicycle_rentals
  AS (
    SELECT COUNT(starttime) as num_trips,
  	     EXTRACT(DATE from starttime) as trip_date
      FROM `bigquery-public-data.new_york_citibike.citibike_trips`
  GROUP BY trip_date
  ),
  	 rainy_days 
  AS (
    SELECT date,
  	     (MAX(prcp) > 5) AS rainy
  	FROM (
  	  SELECT wx.date AS date,
  	         IF (wx.element = 'PRCP', wx.value/10, NULL) AS prcp
  	    FROM `bigquery-public-data.ghcn_d.ghcnd_2015` AS wx
         WHERE wx.id = 'USW00094728'
  	)
  GROUP BY date
  )
  
  SELECT ROUND(AVG(bk.num_trips)) AS num_trips,
  	   wx.rainy
    FROM bicycle_rentals AS bk
    JOIN rainy_days AS wx9
      ON wx.date = bk.trip_date
  GROUP BY wx.rainy
  ```

  - 참고링크:
    - https://logical-code.tistory.com/39
    - https://thebook.io/006696/part01/ch07/02/
    - https://superkong1.tistory.com/35


