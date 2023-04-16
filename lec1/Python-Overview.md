# Programming and Execution Environment (chapter1.1)
[챕터1: Python Overview](https://kooc.kaist.ac.kr/datastructure-2019s/lecture/40273)
##  Programming and DS&A

- 자료 구조 : 설계도, 구조 (어디에 화장실을 만들지)
- 알고리즘 : 동작을 어떻게 하는지 (어떻게 화장실을 가는지)
- 구현 : 프로그래밍 

## Python 

- 컴파일러 : 실행 이전에 프로그램을 최적화 시켜놓고 실행 
- 인터프리터 : 최적화 되지 않아도 일단 실행은 되게 (파이썬)
- Object-oriented : 객체를 설계하고 자료를 구조화 하는 것을 배움 
- Dynamic type of variable : 컴파일러는 타입이 고정임(변수형을 정해줌) 인터프리터는 타입이 동적(다이나믹) 하게 변함 
- Code Structure : PEP8 이나 스타일 가 잘 정리되어 있음 
- Fast Development speed, slow execution speed 
- 데이터 분석에 특화 : Numpy, Scipy, Tensorflow, Pytorch 등  

<br>

# Hello World in Python (chapter1.2)

- Procedure-oriented progam : 함수기반 

```python 

def main(): 
    print("hello world") 
    score1, score2 = input("Enter two scores")
    average = (score1+score2)/2.0; 

    print(average)

main() 
    
```
- Object-oriented class : 클래스 기반 

```python 
class HelloWorld: 
    def __init__(self):
        print("Hello word, Just one more time")
    def __del__(self):
        print("good bye")
    def performAverage(self,val1,val2):
        average = (val1+val2)/2.0 
        print("average:", average)

``` 

- world : Instance storage variable 
- Helloworld() : Instance'template 
- self : 자기 자신의 인스턴스의 값을 쓰는거로 이해 

```python 

def main():
    world = HelloWorld()      
    score1, score2 = input("Enter value")
    world.PeformAverage(score1,score2)

main() 
```

<br>

# Naming and Styling (chapter1.3)
- CamelCase : 대소문자를 섞어서 (ex.HelloWorld)
- 변수명 : 소문자로 시작 (ex.numberOfStudents), 파이썬에서는 데이터타입을 변수명에 넣는걸 추천하지 않음 
- 함수명 : 소문자로 시작 

## Comment   
```
파이썬 함수나 코멘트안에 여러줄의 주석은  ``` 이나 """ 으로 감싸줄 것 
한줄은 # 으로 
```

<br>

# Variable Statements and Operators (chapter1.4)

- 데이터 타입 
<img width="1230" alt="스크린샷 2023-04-09 오후 4 15 35" src="https://user-images.githubusercontent.com/83544197/230759708-401c4e26-f9c3-494c-8e9b-fe123d5ea8cc.png">

- 연산자 : 합,곱,차,나누기 등 


<br>

# String (chapter1.5)
- Python 에서의 Index 인식 
- String 은 결국 Linear Collection 이다. 
- 파이썬에서는 Negative Index 가 가능 

<img width="896" alt="스크린샷 2023-04-09 오후 4 42 32" src="https://user-images.githubusercontent.com/83544197/230760613-c688261a-6697-456f-9003-acd110354447.png">



<br>

# List,Tuple,Dictionary (chapter1.6)
## Index range 

```python 
strTest = "Hello World! ISE" 

print(strTest[0:5:2]) # Hlo 나옴
print(strTest[5::-1]) # olleH  로 나옴 
```

## List 
- 리스트안에 데이터는 어떤 형태든 자유롭게 들어갈 수 있다. 
```python 
lstTest = [1,2,3,4]
print(lstTest[0]) # 1출력 

lstTest.append('key')
print(lstTest) # 1,2,3,4,'key' 출력

```
## Tuple 
- 튜플안에 값 변경이 불가능 (Immutable)
- 나머지는 리스트랑 똑같다고 이해하셈 

```python 
tplTest = (1,2,3) 
print(tplTest[0]) # 1 출력 
```

## Dictionary 
- 더이상 선형적이지 않은 Collection type (Not Sequential)
- key 와 value로 구성되어 있음 
- dictionary 에서는 리스트나  튜플처럼 index 가 아니라 key 로 생각

```python 
dicTest = {1:'one',2:'two'}
print(dictTest[1]) # 'one' 출력 

dicTest[4] = 'four'
print(dictTest[4]) # 'four' 출력 

dicTest.keys() 
dicTest.values() 
dicTest.items() 

```

# Condition and Loop Satement (chapter1.7)

## if 조건문 (condition statement)
- 조건문 안의 block 이 True 일때 실행, False 면 다른 조건문을 실행 
- indentations 는 4칸으로 

## for문 (loop statement)
- 대표적인 loop statement
- contunue, break 같은 statements 도 익힐 것 

```python 
for itr in range(5): 
    if itr == 3: 
        break #  만나면 아예 for 문을 종료 
    print(itr)
else:
    print(',')
print('done')

```

- continue 를 만나면 다시 원래의 loop 로 돌아감 

```python 

for itr in range(1,100,10):
    if ite == 51: 
        continue # 이때 51은 출력이 안 됨 
    else: 
        print(itr)

```

# Function Statement (chapter1.8)
- def fun_name(params): 의 형태 
- 다른 언어랑 다르게 파이썬에서는 결과(return)에 대한 특성을 따로 지정해주지 않아도 됨 (장점이자 단점)
> 장점 : 프로그램 짜기 쉬움 

> 단점 : 향후에 문제가 생길 수 있음
- 콜론을 block statement 라고 부름 

## lambda 함수 
- 한줄로 함수를 처리 할 때 (함수명을 정의할 필요 없을 떄)

```python 
a = lambda x,y : x+y 
a(3,4) # 7 출력 
```
- 만약 소수를 찾는 함수를 만든다면? (for 문에 else 문 들어가는거 익숙해질 것)

```python 

def is_prime_number(numParam1):
    for itr in range(2, numParam1):
        if numParam1 % itr == 0:
            break
    else:
        return True
    return False
            
def find_prime(numParam1,numParam2):
    numCount = 1 
    for itr in range(numParam1,numParam2):
        if is_prime_number(itr) == True: 
            print(f'{numCount}th prime: 1')
            numCount += 1 
    
```

# Assignment and Equivalence (chapter1.9)
- list 도 하나의 element 처럼 볼수 있는가? 
- 아래 케이스에서는 y = [100, x, 120]에서 x에 대한 reference 만 존재함 (not copy)
- **==** 는 두 레퍼런스된 value 를 비교함 
- **is** 는 두 레퍼런스된 id 를 비교함 즉 두 값의 저장장소가 같은가를 확인 (중요)

- x = 'abc' 이거는 x 라는 변수명에 문자열 객체를 할당(Assignment,메모리 할당) 하고 x 는 문자열 객체의 메모리를 참조하기만 하는 역할 

- 객체(Object)는 파이썬에서 모든 것이 객체로 표현됩니다. 모든 객체는 메모리에서 고유한 식별자(주소)를 가지며, 이를 통해 객체에 접근할 수 있습니다. 객체는 데이터와 기능(메서드)으로 구성됩니다.

- 메모리 주소(id) 는 객체가 저장되는 메모리 공간의 주소를 나타내며, 파이썬에서는 id() 함수를 사용하여 객체의 메모리 주소를 확인할 수 있습니다.

- 변수(Variable)는 객체를 가리키는 이름으로, 객체를 할당한 변수는 해당 객체에 대한 참조(Reference)를 갖게 됩니다. 파이썬에서는 변수를 선언할 때, 값을 할당하는 것이 아니라 객체에 대한 참조를 할당합니다.

- 인스턴스(Instance)는 클래스(Class)에서 생성된 객체를 의미합니다. 클래스는 객체의 설계도이며, 인스턴스는 그 설계도에 따라 생성된 실제 객체입니다.

- 객체와 메모리 주소는 다른 개념입니다.
객체는 데이터(변수) 와 메서드(기능)를 포함하는 개념으로, 파이썬에서 모든 것은 객체입니다. 객체는 데이터와 메서드를 가지고 있으며, 이를 통해 기능을 수행합니다.메모리 주소는 객체가 실제로 저장되는 메모리의 위치를 나타내는 값입니다. 객체는 메모리 상의 주소를 갖으며, 이를 통해 객체를 식별할 수 있습니다.객체는 프로그램의 실행 중에 생성되고, 메모리 상에 할당됩니다. 이 때, 각 객체는 메모리 상에서 고유한 주소를 갖습니다. 이러한 메모리 주소는 객체를 식별하는 데 사용되며, id() 함수를 사용하여 확인할 수 있습니다.즉, 객체는 데이터와 메서드를 포함하는 개념이며, 메모리 주소는 객체가 메모리 상에서 저장되는 위치를 나타내는 값입니다.

```python 

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

car1 = Car("Tesla", "red")  # car1은 Car 클래스의 인스턴스입니다.
car2 = Car("BMW", "blue")  # car2도 Car 클래스의 인스턴스입니다.

print(car1)        # 출력: <__main__.Car object at 0x7f9748a2a160>
print(id(car1))    # 출력: 140302338407456 (메모리 주소로 == 0x7f9748a2a160) 
print(car1.model)  # 출력: Tesla
print(car2.color)  # 출력: blue

```

```python
x = [1, 2, 3]
y = [100, x, 120] # nested 
z = [x, 'a', 'b']

x[1] = 1717 # 이 변화가 y,z 에 반영 됨 
print(y) 
# 결과는 아래와 같음 
[100,[1,1717,3],120]

if x[1] is y[1][1]:
    print('equivalent in the same place')
else: 
   print('equivalent not in the same place')     

```
- id() : 해당 객체의 메모리 주소값 반환 
```python 
>>> id(x)
4381942528
>>> id(y)
4381942272
>>> id(y[1])
4381942528
>>> id(y[1][1])
4381991024
>>> id(x[1])
4381991024
```

# Class and Instance (chapter1.10)
- 클래스 : 설계도라고 이해하면 편함 
- 인스턴스 : 만들어진 집 (각각 선언된 인스턴스 끼리는 다른 메모리에 할당 됨)
- Constructor : 언더바 2개 (__)가 앞뒤로 붙은 함수, 인스턴스가 초기 생성할때 Assign 한다고 이해 (ex. \_\_init\_\_)
- Destructor : 파이썬에서 Destructor(소멸자)는 객체가 소멸될 때 호출되는 메서드입니다. 파이썬에서는 객체가 더 이상 사용되지 않을 때 자동으로 메모리에서 해제됩니다. 이때 객체가 소멸될 때, 파이썬은 해당 객체의 소멸자를 호출하여 필요한 정리 작업을 수행할 수 있습니다. (ex. \_\_del\_\_)

```python 

from time import ctime 

class MyHome: # 클래스 선언 

    def __init__(self,strAddress):
        print(strAddress)
        print(f'Built at {ctime()}')

    def __del__(self):
        print(f'Delete as {ctime()}')

homeatDeaJeon = MyHome('Daejeon at KAIST') # 클래스의 인스턴스 생성 

```
# Module and Import(chapter1.11)
- 한 파일안에는 하나의 클래스를 넣는걸 추천함 이것들을 어떻게 엮을 수 있을까? 


## Home Module  
```python 

from time import ctime 

class MyHome: 
    def __init__(self,roof_color): 
        self.roof_color = roof_color 
    
    def print_home_color(self): 
        print(f'my home color is {self.roof_color}')

    def __del__(self): 
        print('delete pacakges')

``` 

## Import Moudel 

```python 

from lec1 import Home 
a = Home.MyHome('red')
a.print_home_color() # 결과는 'red'를 출력 
``` 

## 모듈을 위한 디렉토리 구조 
- 패키지를 위한 directory 구조를 만드는 것을 추천 
- \_\_init\_\_.py 는 해당 폴더가 패키지 라는것을 의미 
- 각 상위 dir 폴더에서 패키지를 불러오는 형태는 좋지 못함 

```python 
from edu.kaist.selab.ie362.week1 import Home 
``` 

- 아래와 같이 src 폴더의 이닛 스크립트에 다음과 같이 넣어주면 
```python 
# src/__init__.py

from .edu.kaist.selab.ie362.week1.Home import Home
```
<<<<<<< HEAD

- 아래처럼 불러 올수 있다. 

```python
from src import Home

my_home = Home('red')
my_home.print_home_color()  # 출력: my home color is red
```
=======

>>>>>>> object-swdesign-3
