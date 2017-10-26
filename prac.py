import turtle as t
import random # 랜덤함수를 생성
a=random.randint(0,359) #a는 0도부터 359도까지 랜덤 설정

#벽만들기
t.speed(0)#가장 빠르게
t.up()#꼬리들기
t.goto(-250,-250)#벽을 그리기 위해 시작점으로 이동
t.down()#꼬리내리기
for x in range(4):
    t.fd(500)
    t.lt(90)
#거북이 중앙으로 가기
t.up()
t.home()
t.down()
#랜덤 설정된 각도로 회전후 벽까지 이동
t.seth(a)
while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
    t.fd(1)# 벽에 부딪히기 전까지 앞으로 1만큼씩 이동
#while True: #아래를 무한 반복
    #a=t.heading()
if 0<a<45:
    t.lt(180-2*a)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if 45<a<90:
    t.rt(2*a)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if 90<a<135:
    t.lt(360-2*a)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if 135<a<180:
    t.rt(2*a-180)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if 180<a<225:
    t.lt(540-2*a)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if 225<a<270:
    t.rt(2*a-360)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if 270<a<315:
    t.lt(720-2*a)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if 315<a<360:
    t.rt(2*a-540)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
if a == 45 or a == 90 or a == 135 or a == 180 or a == 225 or a == 270 or a == 315 or a == 360:
    t.lt(180)
    t.fd(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.fd(1)
