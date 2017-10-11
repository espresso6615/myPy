import turtle as t #거북이생성
n=5                #n을 5로 설정
t.color("skyblue") #선색을 하늘색으로 설정
t.speed(0)         #거북이의 속도를 최대로 설정
a=1                #a를 1로 설정

for x in range(25):# 25번 반복
    a=a+1 #a에 1을 더해서 다시a에 저장
    t.begin_fill() #채우기시작
    for x in range(n):#n번 반복
        t.fd(75)
        t.lt(360/n)
    t.end_fill()#채우기끝
    if a%4 == 1: #a를 4로 나눈 나머지가 1일때
        t.back(75)
        t.rt(144)
    if a%4 == 2: #a를 4로 나눈 나머지가 2일때
        t.fd(75)
        t.lt(288)    
    if a%4 == 3: #a를 4로 나눈 나머지가 3일때
        t.back(75)
        t.rt(144)
    else: # 그외
        t.fd(75)
        t.lt(288)    
