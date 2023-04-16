# Design and Programming(chapter2.1)
[챕터2: Object-oriented paradigm and software design](https://kooc.kaist.ac.kr/datastructure-2019s/lecture/40284?isDesc=false)

##  Object-Oriented Paradigm (OOP)
- 이번 파트에서는 프로그램 설계하는 것을 배움 
- OOP 컨샙 : Class, Instance, Inheritance, encapsulation, polymorphism 
- Unified Modeling Langauge(UML) : 설계도를 읽는 방법 
- 소프트웨어 디자인 : Factory, Adapter, Bridge, Composite, Observe
- **Correctness** 
> Meet the client’s purposes

> Successful implementation without errors

- **Robustness**
>Execute under expected overloads

- **Flexibility** 
> Enable the future updates and expansions of functions

- **Usability and Reusability** 
> Good support for the designed 

> Easy to use for 1) other purposes and 2) other contexts

- **Efficiency** 
> Easy to implement & Smaller size &Faster execution

## OOP의 개념 
- 속성(Attribute) : 값이나 개념의 특성 (=값)
- 메소드(Method) : 개념이 하는 행동 (=함수)

## Class vs Instance 
- Class : 하나의 디자인, 개념화로 이해 (설계도)
- Instance : 클래스에 의해 만들어진 것, 추상적인 것을 실제화 (실제 구현) 
- 고객(Customer) 이라는 클래스에 실제 고객 (Kim, 37세, 남자)의 인스턴스 

# UML Notation (chapter2.2)

## Software Design  
- 커뮤니케이션을 위한 소프트웨어 설계를 위한 **표준**을 알아야 함
- 이런 표준 언어를 UNIFIED MODELING LANGUAGE (UML)이라 함 

## Class and Instance on UML 

<img width="1264" alt="스크린샷 2023-04-14 오후 1 59 18" src="https://user-images.githubusercontent.com/83544197/231945770-17be2991-3a9f-4bf8-9a17-e0d1701cbe71.png">

- Variable 은 attribute, Property 라고도 부름 
> +-#(name):(type)=(default value) 예시로 +Name:String = Kim
- Visibility options 
> \+ 는 public

> \# 은 protected 

> \- -> private 

# Encapsulation and Inheritance (chapter2.3)

## Encapsulation 
- Object = Data + Behavior 

> Data : field,member variable, attribute,

> Behavior : method, member function, operation 

- Delegating the implementation responsibility 
 > 새로운 기능이나 요구사항이 있을 때 기존의 코드를 수정하지 않고 책임을 다른 객체나 모듈에 위임하여 유연성과 확장성을 높이는 방법입니다.

 - Encapsulation 에서 method 는 public 으로 데이터는 private 로 생각 
 > 예를 들어, 은행 계좌 객체를 생각해보면, 계좌 잔액이나 계좌번호 등은 외부에서 직접 접근할 수 없도록 private으로 선언하고, 입금과 출금 같은 기능은 public으로 선언하여 제공합니다. 이렇게 하면 계좌 잔액 등의 데이터가 무결성을 유지하며, 클라이언트는 입금과 출금 같은 기능만 사용하면 되므로 객체의 내부 구현에 대해 알 필요가 없어집니다.
 - 파이썬은 visibility options을 제공은함 (언더스코어2개로 _ _)

 - Getter와 Setter 메소드: Getter와 Setter 메소드는 캡슐화된 속성의 값을 읽고 쓰는 메소드입니다. Getter 메소드는 캡슐화된 속성의 값을 읽기 위해 사용되며, Setter 메소드는 캡슐화된 속성의 값을 쓰기 위해 사용됩니다. 이러한 메소드를 제공함으로써, 클래스 내부에서 캡슐화된 속성에 접근할 수 있는 방법을 제공합니다.

- 내부 클래스: 내부 클래스는 클래스 내부에서만 사용되는 클래스입니다. 이를 통해, 클래스 내부에서만 사용되는 기능을 외부에서는 접근할 수 없도록 제한할 수 있습니다. 내부 클래스는 클래스 내부에 정의되며, 클래스 외부에서는 접근할 수 없습니다.



 ## Inheritance (상속)
- 내 Attribute와 method 들을 상속함, 즉 상속받은 클래스 자체로 새로운 속성을 가짐 
> 예를들면 Person 클래스는 좀더 General 하게 그 아래서 Customer 나 Employee 는 Specialized 됨 

## Super class 
- Generalized from the conceptual view (가장 위에 있는 클래스)

## Subclass 
- 상속받은 객체로 이해 

```python 

class Father: 

    def __init__(self,strHometown):
        self.strHometown = strHometown
        print('Father class')

    def doFatherthing(self):
        print('Father do')

    def doRunning(self): 
        print('slow')
        

class Mother: 

    def __init__(self,strHometown): 
        self.strHometown = strHometown
        print('Mother class')

    def doMotherthind(self):
        print('Mother do')
        
class Child(Father, Mother):
    
    def __init__(self, strHometown):
        super().__init__(strHometown)
        print('Child class')
    
    def doRunning(self):
        print('fast')

me = Child('seoul') 

```
## self and super
- self : 자기 자신의 instance를 의미함
> child 클래스에서는 self.strName = strName 

- super : 자기 위에(상속 해주는) base class의 instance를 의미함
> super(Child,self).\_\_init\_\_(paramHome) 여기서 super(Child,self)는 Father 를 찾음 

# Polymorphism and Abstract Class (chapter2.4)

## Polymorphism 
- Poly : Many, Morph : Shape 으로 이해 
- 유사한 형태(Signature) 를 가지고 있지만 다른 행동(Behavior)을 할때 
- Method Overriding 
> Parent 의 메소드랑 child 의 메소드가 동일할때 Child의 메소드를 사용함 (부모쪽 메소드 무시)

- Method Overloading 
> 어떤 클래스가 같은이름의 다양한 메소드를 가질 수 있음 동일한 이름의 메소드이지만 기능이 다른 경우 

## Abstract class 
- 꼭 구현(Implementation)해야하지만 실제 구현은 안한것 (pass문으로 처리)

- 추상 메소드(abstract method)란 클래스 내에 선언만 되고 구현이 되어있지 않은 메소드를 말합니다. 즉, 추상 메소드는 메소드의 선언부만 있고, 실제 동작하는 내용이 없는 메소드입니다. 추상 메소드는 "abstract" 키워드를 사용하여 선언합니다.

## Overriding Methods in object 
- 모든 파이썬 클래스는 object 의 descendents 이다. 즉 hidden 메소드를 override 한다고 이해
- 히든 메소드 종류 
> \_\_init\_\_, \_\_del\_\_, \_\_eq\_\_, \_\_cmp\_\_, \_\_add\_\_,

- \_\_eq\_\_ : 이퀄리티 체크 (클래스끼리 동등성 체크이며 메모리 체크가 아님)
- \_\_cmp\_\_ : 이퀄리티 체크 (클래스끼리 동등성 체크이며 메모리 체크가 아님)
- \_\_add\_\_ : 이퀄리티 체크 (클래스끼리 동등성 체크이며 메모리 체크가 아님)

# UML notation 2 (chapter2.5)

## More about UML Notations 
- Use-case diagram
- Class diagram
- State diagram
- Deployment diagram 
- 단일 클래스 
<img width="1326" alt="스크린샷 2023-04-16 오후 2 52 25" src="https://user-images.githubusercontent.com/83544197/232274343-ccfa7462-1809-4aa5-996b-d34a05a6a214.png">


## Structures of Classed in Class Diagram 

- 설계도의 화살표에 따라 기능이 다름 
> 삼각형 화살표는 generalizationm, 그냥 화살표는 association, 마름모 화살표는 aggregation 

<img width="1279" alt="스크린샷 2023-04-16 오후 2 54 53" src="https://user-images.githubusercontent.com/83544197/232274410-22e9a117-3236-462b-a997-d372d948ba4c.png">

# Structure and Relationship (chapter2.6)

## Generalization 
- is-a relationship (ex. Customer is a Person)
- Inheritance relationship 
- Customer -|> Person (화살표 주의, Hollow Arrow) 즉 Person은 Customer 의 Generalization

## Association 
- has-a relationship (어떤 클래스가 무엇을 가지고 있다.)
- Member variable 과 연관 (ex. Customer has a number of accounts)
- multiplicity 한 정보를 가지고 있음 
- Simple line 으로 표시하며 Arrow 가 붙은 경우는 아래와 같이 이해 a customer has a ref to bank accounts 

- one to many 나 one to one 같은 관계도 Diagram 드릴 때 주의 할 것 (* 로 표시)

## Multiplicity of Association 

- *는 many를 의미함 
<img width="1120" alt="스크린샷 2023-04-16 오후 3 45 32" src="https://user-images.githubusercontent.com/83544197/232278061-49563717-b579-4cfe-8b5c-1192f5282991.png">


## Aggregation 
- Special has-a relationship
 
<img width="1177" alt="스크린샷 2023-04-16 오후 3 50 21" src="https://user-images.githubusercontent.com/83544197/232278251-811ccd0e-b919-4d13-ae68-c56fed4a80f6.png">


## Dependency 

- use relationship (ex. Engineer use a calculator)
- 해당 메소드가 다른 기능을 활용만 할 떄 

<img width="1117" alt="스크린샷 2023-04-16 오후 3 53 11" src="https://user-images.githubusercontent.com/83544197/232278390-663d52fb-71ce-4317-9dbc-3d1cd8be229c.png">










