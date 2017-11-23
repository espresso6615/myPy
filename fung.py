import turtle as t
import math


x_min = -5
x_max = +5

y_min = -5
y_max = +5

space = 0.1

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)

t.goto(-5,0)
t.goto(5,0)
t.up()
t.goto(0,5)
t.down()
t.goto(0,-5)
t.goto(0,0)


func1 = input("그리고 싶은 함수를 입력하세요1")
func2 = input("그리고 싶은 함수를 입력하세요2")

t.color("red")
x = x_min
exec(func1)
t.up()
t.goto(x,y)
t.down()
list1=[]
while x <= x_max:
    x = x + space
    exec(func1)
    t.goto(x,y)
    a=t.ycor()
    list1.append(a)
#print(list1)
t.color("green")
x = x_min
exec(func2)
t.up()
t.goto(x,y)
t.down()
list2=[]
while x <= x_max:
    x = x + space
    exec(func2)
    t.goto(x,y)
    b=t.ycor()
    list2.append(b)
#print(list2)
s=0
while s < 100:
    if abs(list1[s]-list2[s]) < 0.1:
        print(-5+s*0.1,",",list1[s])
        s=s+1
    else:
        s=s+1
        
        
        
        
        
      

