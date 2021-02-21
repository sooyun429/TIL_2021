## SQL_Oracle



### 연산자

#### LIKE 

- ESCAPE : 와일드 카드 문자를 일반문자 처럼 사용하고 싶은 경우에 사용
  ex) WHERE name LIKE '%a\\_y%' ESCAPE '\\'
- LIKE 연산자는 대소문자를 구분 한다.
- UPPER() 함수를 이용해 대소문자 구분없이 출력 할 수 있다.
  (인덱스 성능문제 발생, 함수기반 인덱스 사용)