## Functions

중요도 

1. 함수(개념, 사용법) - 매개변수와 인자 중요
2.  함수와 Scope - 재귀 함수 - 유용한 함수 

시험에서 중요도

1. 함수와 Scope~packing

### 함수(functions)

: 특정한 작업을 수행하기 위한 재사용 가능한 코드 묶음함수를 사용하는 이유

```
t. 우리가 늘 고민해야할 부분 -> 무한대로 늘려보자!
```

##### 함수를 사용하는 이유

- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상

 ```
 # 두 수의 합을 구하는 코드
 num1 = 5
 num2 = 3
 sum_result = num1 + num2
 print(sum_result)
 
 t. 이것을 열번하는 것보다 함수를 만들자!
 
 # 두 수의 합을 구하는 함수
 def get_sum(num1, num2):
 	return num1 + num2
 	
 # 함수 사용하여 결과 출력
 num1 = 5
 num2 = 3
 sum_result = get_sum(num1, num2)
 print(sum_result)
 ```



#### 내장 함수(Built - in function)

: 파이썬이 기본적으로 제공하는 함수(별도의 import 없이 바로 사용 가능)  (예) print()

```
(파이썬 공식 문서 주소) https://docs.python.org/ko/3.9/tutorial/index.html

t. 빌트인 냉장고를 생각! 파이썬안에 원래 들어가 있는 거
```



- 내장 함수 예시 : 절대값을 만드는 함수 abs

```
#abs 함수 호출의 반환 값을 result에 할당
result = abs(-1)
print(result) # 1
```



- 함수 호출(function call) 

  : 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것


```
t.
def 함수명(매개 변수):
	pass
	

#함수 정의문 : 함수는 항상 인풋과 아웃풋을 생각해야한다.

#함수이름(전달 인자)-> 함수 호출문

ex)
1. 함수 정의문
def test():
	pass
	
2. 함수 호출
test() 
-> 함수를 정의부터 호출까지 해야지 의미를 가진다.
```



#### 함수의 구조

##### 함수 구조

: input (X) [parameter] -> function body [body] (함수 몸체)-> output f(X) [return  value]



##### 함수의 정의와 호출

- 함수의 정의(정의)
  - 함수 정의는 def 키워드로 시작
  - def 키워드 이후 함수 이름 작성
  - 괄호 안에 매개변수를 정의할 수 있음
  - 매개변수(parameter)는 함수에 전달되는 값을 나타냄

```
# 함수의 정의
def greet(name):
	"""입력된 이름 값에 인사를 하는 메세지를 만드는 함수"""
	message = 'Hello, ' + name
	
# 함수 호출
result = greet('Alice')
print(result) # hello, Alice
```



- 함수 body

  - 콜론(:) 다음에 들여쓰기 된 코드 블록 

  - 함수가 실행 될 때 수행되는 코드를 정의

  - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명 (예) """입력된 ~~ 함수"""

    

- 함수 반환 값 / 반환이라는 것은 print와 다름

  - 함수는 필요한 경우 결과를 반환할 수 있음
  - return 키워드 이후에 반환할 값을 명시
  - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환

```
# 함수의 정의
def greet(name):
	"""입력된 이름 값에 인사를 하는 메세지를 만드는 함수"""
	message = 'Hello, ' + name
	return message
	
# print와 return의 다른점
print : ATM에서 잔액이 얼마 있는 지 확인하는 것 / 눈으로 보여주는 것만 가능->즉, 함수를 재생산 못 함
return : ATM에서 돈을 출금하는 것 / 이용할 수 있다는 것
```



- 함수 호출
  - 함수를 호출하기 위해서는 함수의 이름과 필요한 인자(argument)를 전달해야함
  - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수(parameter)에 대입됨

```
# 함수 호출
result = greet('Alice')

# parameter와 argument의 차이점
parameter는 X이고, argument는 X가 받는 값이다. 
```





### 매개변수와 인자

#### 매개변수 (Parameter)

:함수를 **정의**할 때, 함수가 받을 값을 나타내는 변수

#### 인자 (Argument)

: 함수를 호출할 때, **실제로 전달되는 값**

```
def add_numbers(x, y): # x와 y는 매개변수(parameter)
	result = x + y
	return result 

a = 2
b = 3
sum_result = add_numvers(a, b) # a와 b는 인자(argument)
print(sum_result) # 5
```



### 인자의 종류

##### Positional Arguments (위치인자)

: 함수 호출 시 인자의 위치에 따라 전달되는 인자

​	*위치 인자는 함수 호출 시 반드시 값을 전달해야 함

```
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
    
greet('Alice', 25) # 안녕하세요. Alice님! 25살이시군요.    

t. 순서대로 전달
```



##### Default Argument Values (기본 인자 값)

- 함수 정의에서 매개변수(Parameter)에 기본 값을 할당하는 것
- 함수 호출 시 인자(argument)를 전달하지 않으면, 기본값이 매개변수에 할당됨.

```\
def greet(name, age=30) :
    print(f'안녕하세요, {name}님! {age}살이시군요.')

이때, age=30이 기본 인자
greet('Alice') # 안녕하세요. Alice님! 30살이시군요.

t. default 인자가 있으면, 중복된 argument 값을 안적어도 됨.
```



##### Keyword Arguments (키워드 인자)

- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으면, 인자의 이름을 명시하여 전달

```
def greet(name, age) :
    print(f'안녕하세요, {name}님! {age}살이시군요.')
    
print(age=25, name=wony) 이것은 둘다 keyword 인자라서, 실행가능함.
# 안녕하세요, wony님! 25살이시군요.
print(age=25, wony) 이것은 위치와 키워드 인자 둘다 써서, 실행이 불가능함.
# positional argument follow keyword argument. 키워드 인자 뒤에 위치 인자가 따라와서, 에러다!

t. 순서가 바뀌어도 상관이 없는 키워드 인자!
```



##### Arbitrary Argument Lists (임의의 인자 목록)

- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 아에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리

```\
1.
print('hi', 'aaaa', 'aa', 'a') #hi aaaa aa a
print('hi', 'aa', 'a') #hi aa a

print()는 정해지지 않는 개수의 인자를 받을 수 있다.

2.
def calculate_sum(*args):
	print(args)
	total = sum(args)
	print(f'합계 : {total}')
	
calculate_sum(1, 2, 3, 4, 5) 
# (1, 2, 3, 4, 5)  
합계 : 6

# tuple : 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형
	- 0개 이상의 객체를 포함하며 데이터 목록을 저장
    - 소괄호()로 표기
    - 데이터는 어떤 자료형도 저장할 수 있음
    - 가능 : 인덱싱(문자 뽑아내기), 슬라이싱(자르기), 길이(길이) / 불가능 : 변경(안전하다)
# 시퀀스 : 여러 개의 값들을 순서대로 나열하여 저장하는 자료형

t. 임의의 인자 목록이 안 좋은 이유가 몇개가 들어올지 몰라서, 메모리를 미리 많이 차지함. (되도록 비권장)
```



##### Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)

- 정해지지 않은 개수의 키워드 인자의 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리

```
def print_info(**kwargs):
	print(kwargs)
	
print_info(name = 'Eve', age = 30)	# {'name':'Eve', 'age' : 30} / key는 무조건 문자열로 받는다. 

t. dictionary는 key로 빨리 찾을 수 있다.(빨리 조회 가능)
```



##### 함수 인자 권장 작성 순서

- 위치 -> 기본 -> 가변 -> 키워드 -> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함

​		*단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음

```
def func(pos1, pos2, default_arg='default', *args(tuple), kwd, **kwargs(dictionary)):

print('hello', end='')
print('asd') 

#hello asd

print('hello')
print('asd') 

#hello asd
```



### 함수와 Scope(공간)

##### Python의 범위(Scope) / 범위(scope) = 전역 변수, 지역 변수, 유효 범위, 생명 주기

- 함수는 코드 내부에 **local scope**를 생성하며, 그 외의 공간인 **global scope**로 구분

- Scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간 / t. 프로그램이 끝날 때, 죽는다. (= 전역 변수)
  - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능) (= 지역 변수)
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수



##### scope 예시

- num은 local scope에 존재하기 때문에 global에서 사용할 수 없음
- 이는 변수의 **수명주기**와 연관이 있음

```
1.
def my_func():
	num=1
	print('local', num) 

my_func() # local 20
print('global', num) #NameError: name 'num' is not defined

#scope가 다르기때문에 print('global', num)의 num을 실행할 수 없다.
num을 쓸려면, 같은 scope(공간)에 num을 정의해야한다.

t. 스코프는 짧게 살아있어야한다. 전역변수는 모든 곳에 영향을 주지만, 지역 변수는 정해진 곳에만 영향 준다. 
```



##### 변수 수명주기(life cycle)

- 변수의 수명 주기는 변수가 선언되는 위치와 스코프에 따라 결정됨

1. bulit-in scope
   - 파이썬이 실행된 이후부터 영원히 유지
2. global scope(=전역 변수)
   - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지 / 프로그램 종료까지 살아있어서, 메모리에 영향을 준다.
3. local scope
   - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

```
인터프리터 : 
```



##### 이름 검색 규칙(Name Resolution) / (안에서 밖은 됨, 밖에서 안은 안됨)

- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음

- 아래와 같은 순서로 이름을 찾아 나가면, LEGB Rule이라고 부름 / LEGB  rule(1~4앞 글자따서 만듬)

	1. Local scope :  지역 범위(현재 작업 중인 범위)
	1. Enclosed scope : 함수안에 공간
3. Global scope : 최상단에 위치한 범위
4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

*함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

```
t. LEGB 시험내기 좋겠지?
```





##### LEGB Rule 예시

- sum이라는 이름을 global scope에서 사용하게 되면서, 기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨
- sum을 참조시 LEGB Rule에 따라 global에서 먼저 찾기 때문

```c)
** LEGB Rule 예시 시험에 나옴

1.
print(sum) # built-in function sum
print(sum(range(3))) # 3

sum = 5

print(sum) # 5
print(sum(range(3))) # TypeError: 'int' object is not callable
*sum 변수 객체 삭제를 위해 del sum을 입력 후 진행

#range(3) = [0, 1, 2]

2.
a = 1
b = 2

def enclosed():
	a = 10
	c = 3
	
	def local(c):
		print(a, b, c) # 10 2 500 (10, 2, 500 아님! 중간에 쉼표 없음)
		
    local(500)
    print(a, b, c) #10 2 3
    
enclosed()
print(a, b) # 1 2

t. 우리가 대표적으로 실수하는 변수
list = [1, 2, 3] -> (이렇게 적어라!) num_list/ arr/ lst = [1, 2, 3]
map -> (이렇게 적어라!) Map
sum -> (이렇게 적어라!) Sum
```

---여기서 부터 공부

##### Global keyword

- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

```
전역 변수(global variable)
프로그램 내 모든 모듈들을 변수 선언의 유효한 영역으로 취하는 변수

num = 0 # 전역 변수

def increment():
	global num # global num을 로컬 변수로 선언
	num += 1
	
print(num) # 0
increment()
print(num) # 1
 
Q. num += 뭔지 모르겠음.
num += 1
>> num = num + 1

for _ in range(5):
	num = num + 1
	num += 1
print(num)
```



##### Global Keyword 주의 사항

- global 키워드 선언 전에 접근 시

```\
1.
num = 0

def increment(): # SyntaxError : name 'num' is used prior to global declaration
	print(num)
	global num
	num += 1
```



- 매개변수(parameter)에 global 사용 불가

```
num = 0

def increment(num): # 'num' is assigned before global declaration
	global num
	num += 1	
```



##### Global  키워드는 가급적 사용하지 않는 것을 권장 

##### 함수로 값을 바꾸고자 한다면 항상 인자(argument)로 넘기고 함수의 반환 값을 사용하는 것을 권장

```
Q. 무슨 말이고?
```



#### 재귀 함수 / 다시한다. + 돌아간다.

: 함수 내부에서 자기 자신을 호출하는 함수

```
t.
정상
def test():
	pass
	
test()

비정상(재귀 함수)-> 알고리즘 특정 문제 / dfs 문제 풀때
def test(): #death Karmel
	test()
	
test()
```



##### 재귀 함수 특징

- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐

- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

```
t. 재귀함수는 끝나는 상황이 없으면 무한 루프에 빠진다.
```





##### 재귀 함수 예시 - 팩토리얼

- factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
- 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
- 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분활된 문제들의 종합하여 최종 결과를 도출

```)
* 시험) 각각 함수 값 하나가 몇번 호출되는 지 
def factorial(n): # 종료 조건 : n이 
	if n == 0:
		return 1
    return n * factiorial(n-1)
>> factorial(n)함수 안에, factorial(n-1)이 있다. -> 재귀 함수
factorial(3)

t.
3! = 3 * 2!
2! = 2 * 1!
1! = 1

Q. n == 0 (?)
```



##### 재귀 함수는 

###### 1. 종료 조건을 명확히 

###### 2. 반복되는 호출이 종료 조건을 향하도록

```
t. 이를 지키지 않으면, 메모리가 부족하고 알고리즘 문제를 시간내에 못 푼다.
```



### 유용한 함수



##### 유용한 내장 함수

- map(function, interable)

```
map은 반복가능한 int
```





##### map(function[함수], interable[반복 가능한 객체 ex. 시퀀스])(80% 씀)

: 순회 가능한 데이터 데이터(interable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

 -> 이 부분 다시 듣기

```
```





##### zip(3% 씀)

: 임의의 interable을 모아 튜플을 원소로 하는 캬ㅔ

````
# zip

왜 이건 순서대로 묶지?
````



##### lambda 함수

: 이름 없이 정의되고 사용되는 익명 함수 / 간편하게 쓸 수 있지만, 정의해서 보여주는 것이 명시적이다. 

```
t. 이름 없는 함수가 왜 필요할까.
호출명이 없어서, 시간이 지나면 garbage collector에 들어간다. 
-> 한번만 쓰고 사라져도 상관이 없다./ 메모리 낭비가 없다.

def test(n):
	return n * 2
	
test(2) # 4
a = test
a(2) # 4
```



##### lambda 함수 예시

- 간단한 



```
addition = lambda x, y : x + y -> 예시라서 addition이라는 이름을 붙여줌 원래 그냥 lambda만 씀

#map +lambda 
numvers = [1, 2, 3, ,4, 5]
result = map(lambda x : x * 2, numbers)
print(result) # [2, 4, 6, 8, 10]
```



### Packing & Unpacking

packing

```
t. 리스트, 튜플로 담는다. -> 패킹한다.
```

*을 활용한 패킹

numbers=[1,2,3,4,5]

a, *b, c = numbers



a, c 처음과 끝 빼고 다 b에 넣겠다.



print(a) #1

print(b) # [2,3,4]

print(c)  # 5



stack을 낭비하기 싫어서, 

##### unpacking 예시

- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당

lst = [1,2,3]

a,b,c=lst -> unpacking한다.

print(a) #1

print(b) #2

print(c) #3



print('1 2 3') # 1 2 3

results = [1, 2, 3] 

print(result) # [1,2,3]

1. ) for result in results : 

​	print(result, end = '" ") # 1 2 3



2) )print(*results) # 1 2 3

--------상단 이터러블 언패킹 하단 non 이터러블 언패킹



 def test(a,b,c):

​		print(a,b,c)



dic= {'a' : 1, 'b' : 2, 'c' : 3}

test(**dic)



[코드 잘 짠 기준]

1) 코드 타임 / 얼마나 시간이 적게 걸린지
2) 코드가 얼마나 짧은지 / 무조건적이지는 아니나 그럴 가능성이 높다. 



##### *, ** 



#### Module-> 누가 만들어준 함수 / 패키지>모듈(선배 개발자가 만들어 놓음)>함수

한 파일로 묶

재사용하기위한 코드 조각

##### 개요

- 



남의 코드를 쓴다. 남의 코드를 잘 가져다 쓰는 것도 필요하다. 



##### 모듈 예시



##### 묘듈 가져오기

import math

help(math)

```

1.
import math

help(math)
```



##### 모듈 사용하기

##### 모듈을 import하는 다른 방법

##### 모듈 주의사항

*만약 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생

- 마지막에 import된 이름으로 대체됨

````
t. 함수, 모듈, 패키지는 재사용성에 좋다!

함수 : 재사용하기 위한 코드 조각

모듈 : 함수들을 재사용하기 위한 코드 조각 
 
패키지 : 모듈들을 재사용하기 위한 코드 조각
````



### 사용자 정의 모듈

##### 직접 정의한 모듈 사용하기

1. 모듈 my_math.py 작성
2. 두 수의 합을 구하는 add 함수 작성
3. my_math 모듈 import 후 add 함수 호출



### 파이썬 표준 라이브러리

#### 파이썬 표준 라이브러리(Python Standard Library)

:  파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

http://docs.python.org/ko/3/library/index.html



#### 패키지(Package)

: 관련된 모듈들을 하나의 디렉토리에 모아 놓은 것



##### 패키지 사용하기

- 아래와 같은 디렉토리 구조로 작성
- 패키지 3개 : my_package, math, statistics



#### PSL 내부패키지

:

#### 외부 패키지

:

#### PIP

#### 파이썬 패키지 관리자(pip)

$ pip install Djongo 



#### 패키지 사용 목적

: 모듈들의 이름공간은 구분하여 충돌을 방지 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

