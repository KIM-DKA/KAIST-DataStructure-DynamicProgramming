from abc import ABC, abstractmethod

# 추상 클래스 정의
class Shape(ABC):
    # 추상 메소드 선언
    @abstractmethod
    def draw(self):
        pass

# Shape 추상 클래스를 상속받는 자식 클래스 Circle
class Circle(Shape):
    def draw(self):
        print("원을 그립니다.")

# Shape 추상 클래스를 상속받는 자식 클래스 Rectangle
class Rectangle(Shape):
    def draw(self):
        print("사각형을 그립니다.")

# 실행 코드
if __name__ == "__main__":
    shape1 = Circle() # Circle 객체 생성
    shape2 = Rectangle() # Rectangle 객체 생성
    shape1.draw() # 원을 그립니다.
    shape2.draw() # 사각형을 그립니다.