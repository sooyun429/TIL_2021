## | XML



#### | 💻 LECTURE

--------------------------

- [💻 SITE] [TCP SCHOOL - XML INTRO BASIC](http://tcpschool.com/xml/xml_intro_basic)
- [💻 SITE] [TCP SCHOOL - XML](http://tcpschool.com/xml/xml_xslt_template)



#### | 👩‍🏫 개념정리

-------------

##### [마크업 언어]

- HTML과 비슷하게 문자 기반의 마크업 언어(text-based markup language)이지만, HTML처럼 데이터를 보여주는 목적이 아닌, **데이터를 저장하고 전달할 목적으로만** 만들어짐
- XML 태그는 HTML 태그처럼 미리 정의되어 있지 않고, **사용자가 직접 정의할 수 있음**
- XML은 텍스트 데이터 형식의 언어로 모든 XML 문서는 **유니코드 문자로만 이루어짐**



##### [XML의 목적]

- 데이터를 텍스트 형식으로 저장하므로, 소프트웨어나 하드웨어에 독립적으로 데이터를 저장하고 전달할 수 있기 때문에 XML을 사용하면 새로운 운영체제나 프로그램, 브라우저 등에 상관없이 데이터를 안전하고 손쉽게 전달할 수 있음



##### [ XML의 구조 및 문법]

- XML 문서 구조 = XML 프롤로그 부분 + XML 요소 부분(하나 이상)

- XML 프롤로그의 문법:

  ```xml
  <?xml version="XML문서버전" encoding="문자셋" standalone="yes|no"?>
  ```

  - version 속성에는 XML 문서에 사용된 XML의 버전 명시

  - encoding 속성에는 XML 문서의 문자셋(character set)을 명시하며, 기본값은 UTF-8로 설정
  - standalone 속성은 XML 문서가 외부 DTD(Document Type Definition)와 같은 외부 소스의 데이터에 의존하고 있는 문서인지 아닌지를 XML 파서(parser)에 알려주는 역할 (기본값은 no이며, yes로 설정하면 이 문서를 파싱(parsing)할 때 참조해야 할 외부 소스가 없다는 것을 의미)

- **요소와 속성의 차이점**: 정보의 전달이라는 측면에서 보면 XML 요소로 표현하는 방법과 XML 속성으로 표현하는 방법에 큰 차이는 없다. 하지만 속성은 여러 개의 값을 가질 수 없으며, 요소처럼 손쉽게 확장할 수 없다는 단점을 가지며, XML 트리에 포함되지 않기 때문에 다양한 용도로 활용할 수가 없다. **-> 그렇다면 속성은 어떨 때 주로 사용하는가?** (말 그대로, 해당 요소의 속성값으로 나타내고 싶을 때??)

- 노드의 정렬  < xsl:sort > 문법

  ```xml
  <xsl:sort
  
      select = string-expression
  
      lang = { nmtoken }
  
      data-type = { "text" | "number" | qname-but-not-ncname }
  
      order = { "ascending" | "descending" }
  
      case-order = { "upper-first" | "lower-first" } />
  ```

   \- select : 노드를 정렬하기 위해 기준이 되는 키(key)를 명시

   \- lang : 정렬 순서를 결정하는데 사용되는 영문자를 명시

   \- data-type : 텍스트의 타입을 명시

   \- order : 정렬 순서를 명시하며, 기본 설정값은 오름차순

   \- case-order : 대소문자에 의한 문자열의 정렬 순서를 명시하며, 기본 설정값은 대문자가 먼저(upper-first)



##### [XML node]

- XML node란?: W3C XML DOM 표준에 따르면 XML 문서 내의 모든 것은 노드(node)라고 불리는 계층적 단위에 정보를 담고 있다. XML DOM을 사용하면 노드 트리에 포함된 모든 노드에 접근이 가능하다.

  | 노드                      | 설명                                                         |
  | ------------------------- | ------------------------------------------------------------ |
  | 문서 노드(Document node)  | XML 문서 전체를 나타내는 노드                                |
  | 요소 노드(Element node)   | 모든 XML 요소로서 속성 노드를 가질 수 있는 우일한 노드       |
  | 속성 노드(Attribute node) | XML 요소의 속성으로서 요소 노드에 관한 정보를 가지고 있는 노드(요소 노드의 자식 노드는 아님) |
  | 텍스트 노드(Text node)    | XML 문서 내의 모든 텍스트                                    |
  | 주석 노드(Comment node)   | XML 문서 내의 모든 주석                                      |

  - [노드로의 접근법](http://tcpschool.com/xml/xml_dom_nodeAccess)
    1. getElementsByTagName() 메소드를 이용하는 방법

    2. 노드 트리를 연속적으로 탐색하여 접근하는 방법

    3. 노드 간의 관계를 이용하여 접근하는 방법


##### [XML inputType과 dataType의 차이]
