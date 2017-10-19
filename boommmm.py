import turtle as t
import random
#땅그리기
t.goto(-300,0)
t.goto(300,0)
t.up()
target=random.randint(50,200)
t.goto(target-25,2)
t.down()
t.color("green")
t.pensize(3)
t.goto(target+25,2)
t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)
#땅그리기 끝

t.speed(0)
def turn_up():
    t.lt(5)
def turn_down():
    t.rt(5)
def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.fd(15)
        t.rt(5)
    d = t.distance(target, 0)
    t.sety(random.randint(10, 100))
    if d < 25:
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10)
        t.setheading(ang)
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()
