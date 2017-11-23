import math
a = float(input("a?"))
b = float(input("b?"))
c = float(input("c?"))

while a==0:
    print("2차방정식이 아닙니다!!!")
    a = float(input("a?"))
    b = float(input("b?"))
    c = float(input("c?"))


if a!=0:
    print("2차방정식이 맞습니다^^")
    D = b*b-4*a*c
    if D > 0:
        x1 = -b+math.sqrt(D)/2*a
        x2 = -b-math.sqrt(D)/2*a
        print("해가 2개입니다", x1,x2)
    if D == 0 :
        x = -b/2*a
        print("해가 1개입니다", x)
        
    if D < 0:
        print("해가 없습니다!")
