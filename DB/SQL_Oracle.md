## SQL_Oracle

### [연산자]

#### | LIKE 

- ESCAPE : 와일드 카드 문자를 일반문자 처럼 사용하고 싶은 경우에 사용
  ex) WHERE name LIKE '%a\\_y%' ESCAPE '\\'
- LIKE 연산자는 대소문자를 구분 한다.
- UPPER() 함수를 이용해 대소문자 구분없이 출력 할 수 있다.
  (인덱스 성능문제 발생, 함수기반 인덱스 사용)
  
### [함수]

#### | [DECODE](https://gent.tistory.com/227)

- DECODE(VALUE, IF1, THEN1, IF2, THEN2...): VALUE 값이 IF1일 경우 THEN1 값을 반환하고, VALUE 값이 IF2일 경우 THEN2 값을 반환한다.
- DECODE 함수는 조건에 따라 데이터를 다른 값이나 컬럼값으로 추출할 수 있다.
- DECODE 함수 안에 DECODE 함수를 중첩으로 사용할 수 있다.

#### | CASE-WHEN

- CASE 함수는 DECODE함수가 제공하지 못하는 비교연산의 단점을 해결할 수 있는 함수이다.
- DECODE함수에서 비교연산을 수행하기 위해서는 GREATEST, LEAST등의 함수를 사용해야 하지만, CASE함수에서는 조건 연산자를 모두 사용 할 수 있다.
- CASE함수는 IF.. THEN .. ELSE 구문과 비슷 하다. WHEN절 다음에 여러 조건이 올 수 있다.

#### | [ROUND, TRUNC, CEIL](https://coding-factory.tistory.com/295)


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
