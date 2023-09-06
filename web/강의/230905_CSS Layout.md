## CSS Layout

2023.09.05(화)

### CSS Box Model

- 모든 HTML 요소를 사각형 박스로 표현하는 개념
  - 내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되는 개념
  - ![image-20230905095437954](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230905095437954.png)

#### 구성요소

##### Box 구성 요소

- Margin : 이 박스와 다른 요소 사이의 공백 가장 바깥쪽 영역

- Border : 콘텐츠와 패딩을 감싸는 테두리 영역

- Padding  : 콘텐츠 주위에 위치하는 공백 영역

- Content : 콘텐츠가 표시되는 영역

  

##### width & height 속성

- 요소의 너비와 높이를 지정 이때, 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함

​		width랑 height는 border와 content 모두가 가질 수 있는 개념이다.



#### 박스 타입

##### Normal flow

- CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향



##### block & inline

- Block : h1, p, div 

  - 항상 새로운 행으로 나뉨

  - width, height 속성을 사용하여 너비와 높이를 지정할 수 있음.

  - 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함

    (너비를 사용가능한 공간의 100%로 채우는 것)

  - 대표적인 block 타입 태그

    - h1 ~ 6, p, div

      

- lnline : a, span, img

  - 새로운 행으로 나뉘지 않음
  - **width와 height 속성을 사용할 수 없음**
  - 수직 방향
    - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
  - 수평 방향
    - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수 있음
  - 대표적인 inline 타입 태그
    - a, span, img, input
    - 

```html
.index{
	display: block;
}
.index{
	display: inline;
}
```

![image-20230905113029358](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230905113029358.png)

- `margin-right: auto`는 요소의 가로 정렬을 위한 마진 조절에 사용되고, `text-align: left`는 텍스트 컨텐츠의 가로 정렬을 위해 텍스트 요소에 사용됩니다.
- inline 요소를 가운데 정렬을 하려면, text-align : center를 해야한다. + 요소의 부모에 가운데 정렬을 해야된다. 





#### 기타 display 속성

#### inline-block

- inline과 block 요소 사이의 중간 지점을 제공하는 display 값
- block 요소의 특징을 가짐
  - width 및 height 속성 사용 가능
  - padding, margin 및 border로 인해 다른 요소가 밀려남
- 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용



#### None

- 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

```html
.none{
	display: none;
}

<div class="box none"></div>
```



### CSS Layout Position

- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
  - display, position, float, flexbox 등



#### CSS Position

- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
  - 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

```
normal flow 시험에 나옴
```



![image-20230905114459816](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230905114459816.png)



#### Position 유형

1. static
   - 기본값
   - 요소를 normal flow에 따라 배치

```html
    .static {
      /* 기본값 */
      position: static;
      background-color: lightcoral;
    }
```



2. relative

   - 요소를 normal flow에 따라 배치 

   - 자기 자신을 기준으로 이동

   - 요소가 차지하는 공간은 static일 때와 같음

```html
    .relative {
      /* 자신의 static 시점(좌측 상단)의 위치에서 움직임 */
      position: relative;
      background-color: lightblue;
      top: 100px;
      left: 100px;
    }
```



3. absolute

   - 요소를 normal flow에서 제거 

   - 가장 가까운 relative 부모 요소를 기준으로 이동
   - 문서에서 요소가 차지하는 공간이 없어짐
   - **가장 가까운 부모** 중 **static이 아닌 부모**를 기준으로 배치가 됨.

```html
    .absolute {
      /* 집나간 아이 자신의 자리를 버리고 간다 static이 아닌 부모를 찾음*/
      position: absolute; 
      background-color: lightgreen;
      top: 100px;
      left: 100px;
    }
```



4. fixed

   예>scroll top, 네비게이션 바

5. sticky
   - 요소를 Normal Flow에 따라 배치
   - 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨(fixed)
   - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky요소의 자리를 대체
     - 이전 sticky 요소가 고정되어있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문
   - 강사님은 프론트에서 사용한 적없음





### CSS Layout Flexbox

```
여기서 4문제 나옴

23.09.05 과제 2번이 서술형 문제

FLEX-GROW 시험에 나옴
```



#### CSS Flexbox

- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
  - 공간 배열 & 정렬



##### 구성요소

- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

![image-20230905134054430](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230905134054430.png)

- main axis(주축)
  - flex item 들이 배치되는 기본 축
  - main start에서 시작하여 main end 방향으로 배치



- cross axis(교차 축)
  - main axis에 수직인 축
  - cross start에서 시작하여 cross end 방향으로 배치



- Flex Container
  - display : flex; 혹은 display: inline-flex; 가 설정된 부모 요소
  - 이 컨테이너의 1차 자식 요소들이 Flex Item이 됨
  - flexbox 속성 값들을 사용하여 자식 요소 Flex Item들을 배치



- Flex Item 
  - Flex Container 내부에 레이아웃 되는 항목



#### 레이아웃 구성

1. Flex Container 지정
   - Flex item은 기본적으로 행으로 나열
   - Flex item은 주축의 시작 선에서 시작
   - Flex item은 교차축의 크기를 채우기 위해 늘어남



2. Flex-direction 지정
   - flex item이 나열되는 방향을 지정
   - column으로 지정할 경우

display에 value로 들어가는 것이 flex

display : inline, block, inline-block, flex, grid, none



#### Flex-wrap 응용

##### 반응형 레이아웃

- 다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식



##### Margin Collapsing(마진 상쇄)

``` 
시험에 나옴
display : None도 시험에 나옴 <-> visibility: hidden
```

- 디자인적 이유 때문에 마진 상쇄됨. contents가 길어지는 것을 방지
- 두 block 타입 요소의 martin top과 bottom이 만나 더 큰 margin으로 결합되는 현상
- 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함
  - 각 요소에 대한 



##### flex flow

