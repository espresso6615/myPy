
sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

if eval(q) == r:
    print("정답!")
    sc1 = sc1 + 1
else:
    print("오답!")
    sc2 = sc2 + 1

print("정답 :", sc1, "오답 :", sc2)
if sc2 == 0:
    print("당신은 천재입니다!")


            
