import random
def make_question():
    a=random.randint(50,100)
    b=random.randint(0,50)
    op=random.randint(0,2)
    q= str(a)

    if op == 0:
        q=q+"+"
    if op == 1:
        q=q+"-"
    if op == 2:
        q=q+"*"
    q = q + str(b)

    return(q)
sc1 = 0
sc2 = 0
for x in range(5):
    q = make_question()
    print(q)
    ans = input("=")
    r =int(ans)
    if eval(q) == r:
        print("정답!")
        sc1 = sc1 + 1
    else:
        print("오답!")
        sc2 = sc2 + 1

print("정답 : ", sc1, "오답 : ", sc2)
if sc2 ==0:
    print("당신은 천재입니다!")
