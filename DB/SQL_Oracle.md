## SQL_Oracle

### [연산자]

#### LIKE 

- ESCAPE : 와일드 카드 문자를 일반문자 처럼 사용하고 싶은 경우에 사용
  ex) WHERE name LIKE '%a\\_y%' ESCAPE '\\'
- LIKE 연산자는 대소문자를 구분 한다.
- UPPER() 함수를 이용해 대소문자 구분없이 출력 할 수 있다.
  (인덱스 성능문제 발생, 함수기반 인덱스 사용)
  
### [함수]

### [DECODE](https://gent.tistory.com/227)

- DECODE(VALUE, IF1, THEN1, IF2, THEN2...): VALUE 값이 IF1일 경우 THEN1 값을 반환하고, VALUE 값이 IF2일 경우 THEN2 값을 반환한다.
- DECODE 함수는 조건에 따라 데이터를 다른 값이나 컬럼값으로 추출할 수 있다.
- DECODE 함수 안에 DECODE 함수를 중첩으로 사용할 수 있다.

### CASE-WHEN

- CASE 함수는 DECODE함수가 제공하지 못하는 비교연산의 단점을 해결할 수 있는 함수이다.
- DECODE함수에서 비교연산을 수행하기 위해서는 GREATEST, LEAST등의 함수를 사용해야 하지만, CASE함수에서는 조건 연산자를 모두 사용 할 수 있다.
- CASE함수는 IF.. THEN .. ELSE 구문과 비슷 하다. WHEN절 다음에 여러 조건이 올 수 있다.
