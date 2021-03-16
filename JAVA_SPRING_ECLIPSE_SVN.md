## | JAVA

#### [💻 LECTURE]

- [JAVA 강의](https://www.youtube.com/watch?v=tvciu9_jHjQ&list=PLq8wAnVUcTFV4ZjRbyGnw6T1tgmYDLM3P)



#### [💥 ERROR]

- 작동되던 기능이 갑자기 안되는 경우
  - 코드 내 오타가 있는지 찾아본다.
  - Compare history를 통해 코드 변경부분을 집중적으로 살펴본다.



#### [개념정리]

##### [오버로딩(overloading)과 오버라이딩(overriding)]

- 오버로딩: 새로운 메소드를 정의하는 것

- 오버라이딩: 상속받은 기존의 메소드를 재정의하는 것

  ```java
  class Parent {
      void display() { System.out.println("부모 클래스의 display() 메소드입니다."); }
  }
  
  class Child extends Parent {
      // 오버라이딩된 display() 메소드
      void display() { System.out.println("자식 클래스의 display() 메소드입니다."); }
      void display(String str) { System.out.println(str); } // 오버로딩된 display() 메소드
  }
  
  public class Inheritance06 {
      public static void main(String[] args) {
          Child ch = new Child();
          ch.display();
          ch.display("오버로딩된 display() 메소드입니다.");
      }
  }
  
  // 실행 결과
  // 자식 클래스의 display() 메소드입니다.
  // 오버로딩된 display() 메소드입니다.
  ```

##### [intValue()와 parseInt() 메소드의 차이]

- intValue(): Integer 객체에서 int형 값을 추출
- parseInt(): String 객체에서 int형 값을 추출



## | SPRING

#### [💻 LECTURE]

- [Framework 강의](https://www.youtube.com/watch?v=XtXHIDnzS9c&list=PLq8wAnVUcTFUHYMzoV2RoFoY2HDTKru3T)
- [전자정부프레임워크 개발자 교육](https://www.egovframe.go.kr/EgovEduMovie.jsp?menu=4&submenu=3)

#### [개념정리]

##### [DAO / DI / IoC]

- DAO: Data Access Object
- DI(Dependency Injection, 종속성 조립, 부품 조립, Dependency들을 조립하기):

  - 결합력이 낮으면 부품을 보다 간편하게 바꿀 수 있다. (수정이 용이) 대신 부품을 조립해주는 과정, 즉, Dependency Injection 과정이 필요하다.
  - Setter Injection 방법(Setter 함수 사용)과 Construction Injection 방법 (생성자 사용) 두 가지가 있다. 

- IoC(Inversion of Control, 역순) 컨테이너

  - XML 파일 또는 Annotation을 통해 주문서를 작성하고, 주문서에 작성된 부품들을 담는 박스같은 개념
  - Dependency(부품)을 조립하거나 담아둘 떄 역순으로 진행



## | ECLIPSE

#### [💥 ERROR]

- 빌드(컴파일) 오류(.class 파일 자동 생성 안되는 오류) 해결 방법
  - 해당 파일 Build Path 확인
  - Project > Properties > Java Build Path 확인
  - META-INF 폴더 아래 `bxm-application.xml` 파일 > Reference Applications 확인



## | SVN

#### [개념정리]

##### [형상관리 프로세스]

1. Eclipse(IDE) 실행
2. 소스 받아오기(Checkout)
3. 신규 개발 또는 코드 수정
4. (Local test)
5. Commit(개발기 반영)



##### [🤲 SVN과 GIT의 차이점](https://www.slideshare.net/einsub/svn-git-17386752)



##### [🤲 HISTORY 비교]

- 과거 형상 확인은 해당파일(우클릭) > Team > Show History 통해 가능하며, 코드 비교가 필요하면 형상(2개) 선택 후 우클릭하여 'Compare with Each Other' 메뉴를 선택하면 확인 가능



#### [💥 ERROR]

- COMMIT 오류 시
  - (Login incorrect)
    - 프로젝트 > Properties > Bxm Properies > Edit > Password 확인