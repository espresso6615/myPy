import turtle as t
n=5
t.color("skyblue")
t.speed(0)
a=1

for x in range(25):
    a=a+1
    t.begin_fill()
    for x in range(n):
        t.fd(75)
        t.lt(360/n)
    t.end_fill()
    if a%4 == 1:
        t.back(75)
        t.rt(144)
    if a%4 == 2:
        t.fd(75)
        t.lt(288)    
    if a%4 == 3:
        t.back(75)
        t.rt(144)
    else:
        t.fd(75)
        t.lt(288)    
    
    
