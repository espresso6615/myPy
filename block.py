import turtle as t
t.shape("circle")
import random
a = random.randint(0,90)
b = random.randint(-250,250)
t.up()
t.fd(250)
t.lt(90)
t.down()
t.fd(250)
for x in range(3):
    t.lt(90)
    t.fd(500)
t.lt(90)
t.fd(250)
#벽그리기
t.up()
t.back(250)
t.lt(90)
t.fd(500)
t.seth(0)
#시작점으로 이동
if a < 45:
    t.goto(250,b)
    ang = t.towards(-250,-250) #seth 는 항상 반시계로 회전
    
  
if a == 45:
    while a == 45:
        t.goto(250,250)
        t.goto(-250,-250)

if a > 45:
    t.goto(b,250)
    ang = t.towards(-250,-250)
    
   
