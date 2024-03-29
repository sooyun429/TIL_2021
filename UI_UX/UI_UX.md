## UI_UX



### 210314_배달의민족 _주문 요청사항

- ASIS: 요청사항 하단에 '다음에도 사용' 체크박스가 있어서 사용자가 적은 요청사항을 다음 주문에도 사용 가능함
  ![배달의민족_주문 요청사항](https://github.com/sooyun429/TIL_2021/blob/master/UI_UX/images/%EB%B0%B0%EB%8B%AC%EC%9D%98%EB%AF%BC%EC%A1%B1_%EC%A3%BC%EB%AC%B8%20%EC%9A%94%EC%B2%AD%EC%82%AC%ED%95%AD.jpg?raw=true)
- 문제상황: 가게ID와 상관없이 요청사항은 그대로 남아 있어, 전혀 상관없는 요청사항이 기록되어 있거나, 주문내용에 따라 결국 요청사항을 새로 작성해야 하는 상황이 생김 😂
  ![배달의민족_주문 요청사항2](https://github.com/sooyun429/TIL_2021/blob/master/UI_UX/images/%EB%B0%B0%EB%8B%AC%EC%9D%98%EB%AF%BC%EC%A1%B1_%EC%A3%BC%EB%AC%B8%20%EC%9A%94%EC%B2%AD%EC%82%AC%ED%95%AD2.jpg?raw=true)
- 개선방법:
  - 가게 ID별 요청사항이 저장되도록 데이터 저장 구조 및 프로세스 변경 필요 -> 가게ID별 요청사항이 저장되는 프로세스의 경우 저장되는 데이터의 양이 기하급수적으로 늘어날 가능성이 있음. 결국 디비 사용량 증가의 문제가 발생함.
  - 최신순 또는 사용량순으로 최대 5개 정도의 요청사항을 저장하는 방법 -> 모든 요청사항을 저장하지 못한다는 측면에서 사용자 편의성이 떨어질 수 있음. 또한 최신순 또는 사용량순으로 정렬 또는 계산작업이 들어가면 결국 디비성능 저하를 초래할 수 있음.



### 210321_롯데마트 무인계산기

![롯데마트 무인계산기](https://github.com/sooyun429/TIL_2021/blob/master/UI_UX/images/%EB%A1%AF%EB%8D%B0%EB%A7%88%ED%8A%B8%20%EB%AC%B4%EC%9D%B8%EA%B3%84%EC%82%B0%EA%B8%B0.jpg?raw=true)

- 이마트 SCO(Self Checkout Machine)와 같은 무인계산기가 청량리 롯데마트에도 생겨났다. 일대일 대응식의 비교는 어렵겠지만, 롯데마트 무인계산기를 사용해보고 느낀 점을 정리해보려고 한다.
  - 종량제봉투(장바구니) 구매 시 결국 매장 직원이 처리를 돕는 프로세스가 수반된다. 이 부분이 자동화 될 수 있는 방법은 없을지 고민해보면 좋을 것 같다.
  - 퇴장 시 매장 직원이 출구에서 영수증을 검사(?)한다. 결국 사람이 필요하다는 한계가 여기서도 느껴졌다.
  - 이마트 SCO의 경우에는 계산을 하게되면 바코드 입력 처리가 완료된 물품을 오른쪽에 올려두어야만 계산이 진행된다(저울 측정을 통해 무게를 비교해서 처리하는 식). 결과적으로 무인계산기를 구축하는 비용은 이마트 SCO가 더 많이 들고, 인건비는 롯데마트 무인계산기가 더 많이 드는 셈이다. 데이터를 쌓아갈수록 양사 방식의 효율성을 비교해볼 수 있으면 좋을 것 같다.
