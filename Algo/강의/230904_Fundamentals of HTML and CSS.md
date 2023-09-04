## Fundamentals of HTML and CSS

2023.09.04(월)

교과서 https://developer.mozilla.org/en-US/docs/Web/HTML/Element/

설치할 것 

1. live server

- 프론트, 백, DB 구조 공부하기

### 웝 소개

#### World Wide Web

- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 공유하는 거대한 정보 공간

  

#### web

- web site, web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술



#### web site

- 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간



#### web page

- HTML, CSS 등의 웹 기술을 이용하여 만들어진, "web site"를 구성하는 하나의 요소
  - HTML "structure" / CSS "styling" / Javascript "Behavior"



### 웹구조화

#### HTML

- HyperText Markup Language  웹 페이지의 의미와 구조를 정의하는 언어

- 연산, 반복이 불가능하여, 프로그래밍 언어가 아님 > 잘 못 사용했을 때, 이상하게 출력되거나 누락된다.

  해결방법 > 개발자 도구로 해당범위에 무슨 문제가 있는 지 살펴볼 수 있다. 

```
- HTML은 왜 의미를 정의하는 언어인가.
tag를 통해서, 컴퓨터에게 우리가 무엇을 할지 전달 할 수 있다. 이에 대한 예시로, title을 들수 있는 데, 우리가 사이트의 제목에 무엇을 붙일 지 컴퓨터가 인식할 수 있도록 함
하지만, 현실적으로 정확한 tag로 의미를 부여하는 것이 어려워 <div></div>로 개발자들은 난발한다. 
```



#### Hypertext

- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트



#### Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 ex) html, Markdown



#### Structure of HTML

##### HTML 구조

```
- <!DOCTYPE html>
	DOCTYPE(Document Type) 문서의 타입이 무엇인지 선언하는 것 > 브라우저가 해석함.
	위의 의미는 해당 문서가 'html:5'로 문서라는 것을 나타냄.
	* front-end에서 하는 질문: Doctype.이 뭔가여?
	* html5의 5는 버전이다.(23 기준 5 최신이다.)
	
- <html></html>
	전체 페이지의 콘텐츠를 포함

- <html lang="en"></html>
	이 문서가 어떤 포멧으로 읽히는 지 알려줌. 영어로 읽힌다.
	
- <title></title>
	브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
	ex) <title>My Page</title> # 페이지 이름이 My Page가 됨
	
- <head></head>
	html 문서에 관련된 설명, 설정 등 
	사용자에게 보이지 않음

- <meta chatset="UTP-8"> 
	meta data의 meta는 '~에 대한'
	encoding 방식이 UTP-8이다.
	<meta charset=”utf-8″> is an HTML tag that is used to indicate the web page's character encoding. In order to see the correct content, the tag's function is used which let the browser know what character encoding was used in the HTML document. The tag is located in the document's head.

- <body></body>
	페이지에 표시되는 모든 콘텐츠
	
- <meta name="viewport" content="width=device-width, initial-scale=1.0">
	어떠한 모니터로 오픈해도 비율이 유지된다.
	
* self closing tag(닫는 태그가 없는 것)
- meta
- image
```



##### HTML Element(요소)

하나의 요소는 여는 태그와 닫는 태그 그리고 그 안에 내용으로 구성됨

닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

```
시험. 요소에 대하여, 맞는 것 틀리는 것을 찾아라.
```



##### HTML Attributes(속성)

규칙

- 속성은 요소 이름과 속성 사이에 공백이 있어야 함
- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
- 속성 값은 열고 닫는 따옴표로 감싸야 함

목적

- 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
- CSS에서 해당 요소를 선택하기 위한 값으로 활용됨



#### Text Structure

##### HTML Text structure

- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것

```
<h1>Heading</h1>
  - 예를 들어 h1요소는 단순히 텍스트를 크게만 만드는 것이 아닌,
	현재 문서의 최상위 제목이라는 의미를 부여하는 것
```



##### 대표적인 HTML Text structure

- Heading & Paragraphs(주제를 가진 문단)
  - h1~6, p
- List
  - ol(ordered list: 순서가 있는 리스트), ul(unordered list: 순서없는 리스트), li(list)
- Emphasis & Importance
  - em(기울기), strong(굵게)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>main heading</h1> /* 대주제를 의미 h1은 구조적으로 하나만 권장을 한다. 더 쓸 수는 있다. */ 
    <h2>sub heading</h2>
    <p>this is my page</p>
    <p>this is <em>emphasis</em></p> /* 기울임 */
    <p>Hi my <strong>name is</strong> air</p>
    <ol>
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹</li>
    </ol>
    <ul>
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹</li>
    </ul>
</body>
</html>
```



### 웹스타일링

#### CSS(Cascading Style Sheet)

- 웹 페이지의 디자인과 레이아웃을 구성하는 언어

```
Cascading 연속화, 위에서 아래로 흐르는
cascade 계단식 : 동일한 우선순위를 같는 규칙이 적용될 때, CSS에서 마지막에 나오는 규칙이 사용됨
비유적으로 위에서 떨어지는 폭포를 생각하거라!
```



###### CSS 구문

```
h1{
	color: blue;
	font-size: 30px;
}

여기서,
선택자 h1 
선언 color: red;, font-size: 30px;
속성 color, font-size
값 red, 30px
```



##### CSS 적용 방법

1. 인라인 스타일
   - HTML요소 안에 style 속성 값으로 작성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
	<h1 style="color:blue; background-color: yellow;">Hello World!</h1>    
</body>
</html>
```



2. 내부 스타일 시트
   - head 태그 안에 style 태그에 작성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1{
			color: blue;
			font-size: 30px;
		}
    </style>
</head>
<body>
	
</body>
</html>
```



3. 외부 스타일 시트
   - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<link rel="stylesheet" href="style.css"
    <title>Document</title>
</head>
<body>
	
</body>
</html>

-----------------별도의 파일----------------

/* style.css */

h1{
	color: blue;
	font-size: 30px;
}
```



#### CSS 선택자

##### CSS Selectors

- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자



##### CSS Selectors 종류

- 기본 선택자
  - 전체(*) 선택자
    - HTML 모든 요소를 선택
  - 요소(tag) 선택자
    - 지정한 모든 태그를 선택
  - 클래스(class) 선택자('.'(dot))
    - 주어진 클래스 속성을 가진 모든 요소를 선택
  - 아이디(id) 선택자('#')
    - 주어진 아이디 속성을 가진 요소 선택
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
  - 속성(attr) 선택자 등
- 결합자(combinatiors)
  - 자손 결합자(" "(space))
  - 자식 결합자(>)



##### CSS Selectors 예시

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 전체 선택자 */
    * {
      color: red;
    }
    /* 타입 선택자 */  
    /* 모든 h2 요소의 텍스트 색을 주황색으로 변경 */
    h2{
      color: orange;
    }

    h3, h4{
      color: blue;
    }
    /* 클래스 선택자 */  
    /*'.'=class을 통해서, 스타일을 재사용할 수 있다.*/
    .green{
      color: green;
    }
    /* id 선택자 */  
    /* # = id 하나의 스타일링 변경할 수 있다. 권장함. 다른 글자도 변경가능하지만, 권장하지 않음*/
    #purple{
      color: purple;
    }

    /* 자식 결합자 */
    .green > span{
      font-size: 50px;
    }

    /* 자손 결합자 */
    .green li{
      color: brown;
    }
  </style>
</head>

<body>
  <h1 class="green">Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <ul class="green">
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
</body>

</html>
```



#### 우선순위

###### Specificity(우선순위)

- 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성 했을 때 어떤 규칙이 적용 되지는 결정하는 것



##### 우선순위가 높은 순

1. Importance

   - !important : 다른 우선순위 규칙보다 우선하여 적용하는 키워드

     Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음

2. Inline 스타일

3. 선택자

   - id 선택자 > class 선택자 > 요소 선택자

4. 소스 코드 순서



#### 상속

##### CSS 상속

- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임



##### 상속 여부

- 상속 되는 속성
  - Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 속성
  - Box model 관련 요소 
  - position 관련 요소



#### 참고

##### HTML 관련 사항

- 요소 이름은 대소문자를 구분하지 않지만, 소문자 사용을 권장

- 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 큰 따옴표 권장

- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성시 주의

  

##### CSS 인라인 스타일은 사용하지 말 것



