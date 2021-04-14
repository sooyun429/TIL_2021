## RETAIL_물류유통

### 유통기한 관리
- 위생관리, 유통기한 관리 문제제기:
- [편의점 가공식품, 유통기한 관리 안 되는 이유](https://www.thescoop.co.kr/news/articleView.html?idxno=25150)
- [편의점 식품안전관리 ‘구멍’...유통기한 지난 곰팡이·변질 식품 판매 다반사](https://www.consumernews.co.kr/news/articleView.html?idxno=608347)
- 바코드의 중요성
- [Information-rich barcodes](http://justfooderp.com/blog/6-tools-for-better-shelf-life-management/)
One of the most useful tools for keeping your integrated software informed with real-time, accurate data are barcodes and scanners. With them you can achieve three things:
Make your operation more efficient by reducing effort;
Eliminate transcription errors;
Easily capture variables that are too hard to capture manually for every item (like expiry dates).
- [QR코드(다이소 사례)](QR코드 계산법으로 아성다이소 물품 다양성을 엿보다)



### 대형마트 / 슈퍼 or SSM / 편의점 (오프라인 vs 온라인 중 오프라인으로 한정하여 논의하기로 한다.)
- 슈퍼(또는 SSM)과 편의점의 차이는 가공(DRY)식품과 신선(WET)식품을 다루는지 등에 대한 차이로 나뉜다. (쉽게 말해, 저온냉장고 필요유무에 따라 나뉜다.)
- 대형마트와 슈펴(또는 SSM)의 차이는 문화시설, 생활용품 등의 포함 유무에 따라 나뉜다.

### SKU(Stock Keeping Unit): 재고 보관 단위
- 상품 관리, 재고 관리를 위한 최소 분류 단위로 개별적인 상품에 대해 재고 관리 목적으로 추적하기 위한 식별 관리 코드

### [EAN-13 (국제 상품 번호)](https://ko.wikipedia.org/wiki/국제_상품_번호)
- EAN-13 바코드로 변환하려면 숫자값은 먼저 3개의 그룹으로 나뉜다. (첫 번째 숫자, 6개 숫자 한 그룹, 나머지 6개 숫자 한 그룹) 
- 첫 번째 숫자가 0이면 첫 번째 그룹의 모든 여섯 개 숫자는 UPC에 쓰이는 패턴을 이용하여 부호화하므로 UPC 바코드는 첫 번째 숫자 집합이 0으로 된 EAN-13 바코드로도 된다.

### 스크랩예정이란?
- 재고가 많거나 한 경우 발주는 안 되고 판매만 가능한 운영 상태

### PL(Private Label)
- 롯데마트에서는 PB(Private Brand라고 함)

### OEM / ODM 
- OEM(Original Equipment Manufacturing, 주문자 상표부착 생산)
- ODM(Original Development Manufacturing, 주문자 개발 생산)

### 납입경로(발주경로): DC/TC/직납/크로스도킹

- 직납: 본부 또는 점포에서 발주 후 협력회사에서 해당 점포에 바로 납품
- WMS(Warehouse Management System, 창고관리시스템)  중 물류배송 형태에 따른 명칭이다.
- DC(Distribution Center) - 보관형 물류 기능으로 물류센터 내에서 제품을 보관하다가 발주시 점포로 점출하는 형태
- DC는 DC Reorder와 DC Repeat 과정으로 나뉜다.
- TC(Transport Center) - 통과형 물류 기능으로 물류센터 납품시 점포별 발주량에 대해 점별로 따로 검수 및 매입을 거치는 물류 형태
- [유통의 거래형태](https://m.blog.naver.com/PostView.nhn?blogId=wookwook5265&logNo=220366228754&proxyReferer=https:%2F%2Fwww.google.com%2F): 직매입(사입) / 특정매입(외상매입) / 임대차 계약
- DC/TC관련 기사: [1위 이마트 놔두고... 공정위, 'DC물류' 많은 롯데마트 먼저 칼댔다(190123_시장경제)](http://www.meconomynews.com/news/articleView.html?idxno=19946)
- [DC/TC/크로스도킹 간단설명](https://linked2ev.github.io/ecommerce/2019/02/13/Ecommerce-news_20190213/)
- [DC/TC 장단점 비교](https://m.blog.naver.com/PostView.nhn?blogId=zldzkfn&logNo=110032597630&proxyReferer=https:%2F%2Fwww.google.com%2F)
- DC/TC 비교
![TC DC PC_1](https://github.com/sooyun429/TIL_2021/blob/master/images/TC%20DC%20PC_1.jpg?raw=true)
![TC DC PC_2](https://github.com/sooyun429/TIL_2021/blob/master/images/TC%20DC%20PC_2.jpg?raw=true)

### DPS/DAS/PAS 설명
- https://m.blog.naver.com/jackshin01/221039015878
- [DAS: Digital Assorting System (코텍전자)](http://www.e-kotech.co.kr/sub02_03.php)

### POG(Plan of Program)란?
- 플래노그램(Plan-O-Gram)
- 판매 데이터를 기반으로 만들어진 진열 프로그램
- 상품 진열 계획 및 배치
- 카테고리별 판매율이 높거나 낮은지, 재고가 많거나 적은지에 따라 데이터를 분석하여 진열을 조정
- 진열 공간대비 매출의 효율성 분석

### POP(Point of Purchase)
- 판매 시점 광고물
- 매장에서 소비자의 상품 구입을 돕기 위한 광고 일체

### 바이어와 AS바이어란? (매입-MD)
- 매입파트 수행업무: 다른 유통업체와 차별화된 상품을 매입해야 하는 매입부서는 이마트에 입점 될 상품과 가격을 결정하고, 어느 매장에서, 어떤 방식으로 판매할 지 등 상품 매입과 판매에 관한 모든 것을 결정하고 판단하는 업무를 진행. 매입업무는 크게 2가지고 직무로 나누어짐.
- 바이어: 이마트에 투입되는 모든 상품과 가격을 결정하고, 신문 광고, 행사 대품 등 주요 행사에 대한 기획 및 결정, 매장 내 구현되는 ISP(Internet Secure Payment 일반결제서비스) 및 판매 방법에 대한 지침 관련 유관부서 협의 등의 업무를 담당. 이런 활동을 통해서 담당 분류의 매출액, 이익액 2가지 목표를 달성해야 함.
- AS바이어/컨트롤러: 바이어가 상품에 대한 기획과 가격 결정에 업무가 집중되어 있다면 AS바이어는 재고 관리 및 매장의 요청사항 처리 등의 지원업무를 담당. 또한 오픈점, 리뉴얼 점포 레이아웃 및 진열 작업을 진행.
[참고링크](http://www.educe.co.kr/company/jobinfo_view.php?sma_no=958&keyword=&search_txt2=)

### SCM(Supply Chain Management, 공급망 관리)
![SCM 흐름도](https://github.com/sooyun429/TIL_2021/blob/master/images/SCM%20%ED%9D%90%EB%A6%84%EB%8F%84.gif?raw=true)

