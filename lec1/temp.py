
def main(): 
    print("hello world") 
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    score1 = float(score1)
    score2 = float(score2)
    average = (score1+score2) / 2.0
    return average 


main()

strTest = "Hello World! ISE" 

print(strTest[0:5:2]) # Hlo 나옴

lstTest = [1,2,3,4]
print(lstTest[0]) # 1출력 

lstTest.append('key')
print(lstTest) # 1,2,3,4,key 출력


numScore = 80  

if numScore <= 80: 
    print(f'{numScore}')
elif numScore <= 70: 
    print('value is lower than')

def main(): 
    for itr in range(0,5):
        if itr == 3: 
            break 
        print(itr)
    print('done')


a = lambda x,y : x+y 

a(3,4)

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    if element == 6:
        print("Element found")
        break
else:
    print("Element not found")

x = [1, 2, 3]
y = [100, x, 120] # nested 
z = [x, 'a', 'b']

x[1] = 1717 # 이 변화가 y,z 에 반영 됨 

y[1][1]

x[1] is y[1][1]

id(x[1])
id(y[1][1])

class MyHome: 
    colorRoof = 'red'


a = MyHome()
b = MyHome() 


id(a)
id(b)

from time import ctime 

print(f'Built at {ctime()}')


import importlib
import Home 

importlib.reload(Home)

from lec1 import Home 

help(Home)

a = Home.MyHome('red')

a.print_home_color()


while True:
    x = input("Enter a number: ")
    if x == "0":
        break
    print(int(x) * 2)