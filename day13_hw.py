import turtle as t
import random # 랜덤함수를 생성
t.shape("circle")
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
while True: #아래를 무한 반복
    b=t.heading() # 현재 바라보는 각도를 저장
    if 0<b<45 or 135<b<180 or 225<b<270:
        if -250 < t.xcor() < 250  : #좌우 500범위 내에서 벽에 부딪히면
            t.seth(360-b)
            t.fd(1)
            while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
                t.fd(1)
        else: 
            t.seth(180-b)
            t.fd(1)
            while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
                t.fd(1)
    if 45<b<135 or 270<b<315:
        if -250 < t.xcor() < 250 : #좌우 500범위 내에서 벽에 부딪히면
            t.seth(360-b)
            t.fd(1)
            while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
                t.fd(1)
        else:
            t.seth(540-b)
            t.fd(1)
            while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
                t.fd(1)
    if 180<b<225 or 315<b<360:
        if-250 < t.xcor() < 250 : #좌우 500범위 내에서 벽에 부딪히면
            t.seth(360-b)
            t.fd(1)
            while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
                t.fd(1)
        else:
            t.seth(540-b)
            t.fd(1)
            while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
                t.fd(1)
    if a == 0 or a == 45 or a == 90 or a == 135 or a == 180 or a == 225 or a == 270 or a == 315 or a == 360:
        t.lt(180)
        t.fd(1)
        while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
            t.fd(1) #각 모서리와 직각에서는 무조건 180도회전하여 진행
