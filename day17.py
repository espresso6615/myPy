import turtle as t
import random

#벽만들기
t.speed(0)
t.up()
t.goto(-250,-250)
t.down()
for x in range(4):
    t.fd(500)
    t.lt(90)
t.bgcolor("orange")
#악당거북이
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)
#먹이
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)
#주인공거북이
t.shape("turtle")
t.color("white")
t.speed(0)
t.up()
t.goto(0,0)

game = True
def turn_up():
    t.seth(90)
    
def turn_right():
    t.seth(0)
    
def turn_left():
    t.seth(180)
    
def turn_down():
    t.seth(270)
    
def play():
    t.fd(10)
    ang = te.towards(t.pos())
    te.seth(ang)
    te.fd(9)
   
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.listen()
score = 0

while game:
    play()
    
    g=t.distance(ts)
    
    if g<10:
        a=random.randint(-250,250)
        b=random.randint(-250,250)
        ts.goto(a,b)
        print("먹었다!")
        score+=1
        print(score)
        
    d=t.distance(te)
    if d<10:
        print("잡혔다!")
        print("총점수:",score)
        game= False
        
    




    
    



         
