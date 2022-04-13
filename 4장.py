#!/usr/bin/env python
# coding: utf-8

# # 함수

# ## 사용자 정의 함수
p.50의 사용자 정의 함수 double(num)을 리턴값이 있게 써 보자.
# In[ ]:


def double(num):
    return num * num

result = double(3)
print('%d의 제곱: %d' % (3, result))  #이 syntax 좀 헷갈리게 생긴 놈이다. 야! 너 와꾸 이상함!!


# ## 복수 반환 (p.50)

# In[ ]:


def swap(a,b): #함수 swap 정의
    temp = a
    a = b
    b = temp
    #print("일단 swap(a,b) 함수 안의 temp, a, b 값은 각각:", temp, ',', a, ',', b)
    print("temp = %d, a = %d, b = %d" % (temp, a, b)) #교수님 따라서 %를 이용해 보니 훨씬 간단하다.

a=3
b=5
swap(a,b)
print('결과적으로 a =', a, ', b=', b)


# 역시 위에처럼 하니 swap이 잘 안 된다. 하하.

# In[ ]:


def swap(a,b):
    return b, a
a = 3
b = 5
a, b = swap (a,b)
print('a=', a, 'b=', b)

이러니까 잘 되죠? 지렸지.
# ### Quiz 4.1 (p.52)

# In[ ]:


def sum(n):    # sum(n)이라는 함수를 선언한다.
    sum = 0    # 이렇게 sum = 0이라고 꼭 선언(+ 0이라고 값까지 초기화)한 다음에 써 줘야 한다. 
               #안 그러면 local variable sum referenced before assignment! 막 이래.
        
    for i in range(1,n+1): #range 파라미터? 아규먼트? 왜 (1,n+1)이라고 썼는지 알갯지? 이래야지 1부터 n까지 잘 나오니까.
        sum += i
    return sum

print(sum(10))    


# In[ ]:


def factorial(n):
    result = 1  # 파이썬의 유연한 점: int result라고 안 했으나, 1이라는 값만 넣어도 알아서 int형이 된다.
    #print(type(result))
    
    for i in range(n):
        result = result * (i+1)  #result *= i+1
    return result
print('3!=', factorial(3))

하하. 퀴즈 두 개 다 깜찍이 손으로 잘 풀어 봤다.
# # Turtle 라이브러리 맛보기 (p.53)
https://docs.python.org/3/library/turtle.html
여기에서 코드를 복붙만 해 보자. Jupyter Notebook에서 잘 돌아가나 보게.Jupyter에서 코드 돌아가는 창이 (응답 없음)으로 떠도 그러려니 하자. 그냥... 세상에는 이런 일도 있는 법이다...from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
# In[ ]:


import turtle
turtle.forward(100)


# In[ ]:


import turtle as t
t.shape('turtle') #turtle의 모양을 turtle로 바꿀 수 있다!!! ^^
t.forward(100)


# ## Turtle로 사각형 그리기
Turtle로 사각형을 그려 보자. (전지적 시점에서 생각하지 말고, 거북이 시점에서는 이래야 사각형이 나온다.)
# In[ ]:


import turtle as t # 그냥 import turtle이라고 안 하고 import turtle as t라고 하면 t.forward 뭐 이렇게 개빨리 타자 칠 수 있다.
t.shape('turtle') # 맨날 turtle.forward ㅇㅈㄹ 할 순 없잖아.

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

이 사각형 그리는 걸 for문으로도 해 보자.
# In[ ]:


import turtle as t
t.shape('turtle')

for i in range(4): #for _ in range(4)라고 해도 된다.
    t.forward(100)
    t.right(90)


# ## 갑자기 분위기 Turtle로 직각삼각형 (p.55)

# In[ ]:


import turtle as t
t.shape('turtle')
t.forward(100)
t.right(90)
t.forward(100)

import math
t.right(90+45)
t.forward(math.sqrt(100*100*2)) #빗변의 길이 계산 후 선긋기 (시간 없어서 수학식 아직 이해는 x)


# In[ ]:


# math 라이브러리 없이 좌표평면을 이용해서 이럴 수도 있다.

import turtle as t
t.shape('turtle')

t.forward(100)
t.right(90)
t.forward(100)
t.setpos(0,0) #goto(), setposition()도 가능.


# ## Turtle로 원 그리기. p. 57
Quiz 4.2: 원 안의 직각삼각형 그려 보기. 둘 중 뭘 먼저 그려도 상관없지만, 책에서는 화살표를 보아하니 원을 먼저 그렸나 보다.

여튼 이 문제로 방향잡기 + setpos()를 잘 익혀 보자.
# In[ ]:


import turtle as t
t.shape('turtle')

t.forward(100)
t.right(45)

t.circle(-100) #반지름 100인 원을 우측에 그린다.

t.right(45)
t.forward(100)
t.right(90+45)

t.setpos(0,0)


# ## 터. 꾸. (Turtle 꾸미기) - p.58
작은 빨간 원 밑 큰 파란 원 그리기.
아 갑자기 대선 결과 생각하니까 하나도 안 웃기네.
# In[ ]:


import turtle as t
t.shape('turtle')

t.color('red')
t.begin_fill()
t.circle(50)
t.end_fill()

t.color('blue')
t.begin_fill()
t.circle(-100)
t.end_fill()


# ## 칸딘스키 그래픽 소스
p.62에 나와 있는 칸딘스키풍 그래픽의 소스가 있다. 22년인데 이걸 내가 전부 베껴 쓸 필요는 없지 당연히!
<<< 그렇지만, 붙여넣은 후 내용이 뭔지 해석해서 나만의 주석을 달아 보래. >>>    <- 이건 중요

"남이 써 놓은 내용을 해석하는 능력이 (제일) 중요합니다."

맞아요 '외로운 천재'는 말도 안 되는 신화야!
사실 빈센트 반 고흐도 테오도르 반 고흐와 요한나 반 고흐-본헤르가 없었으면 세상에 나오지 못했을 거라고.
사실 3인 팀이라고!!!

그런 의미에서 협업 사회! 가자고!!!
# In[ ]:


import turtle # 그림 그리게 turtle 라이브러리 가져옴
import random # 늘 새로운 그림이 나오게 random 라이브러리 가져옴

for i in range(10):
    
    for j in range(5):
        
        # col로 랜덤한 선 색 고르기. j로 인해 5번 반복된다.
        col = random.randint(0, 3)
        if (0 == col):
            turtle.pencolor("yellow")
        elif (1 == col):
            turtle.pencolor("blue")
        elif (2 == col):
            turtle.pencolor("red")
        elif (3 == col):
            turtle.pencolor("green")
        
        # col로 랜덤한 면 색 고르기. j로 인해 5번 반복된다.
        col = random.randint(0, 4)
        if (0 == col):
            turtle.color('red')
        elif (1 == col):
            turtle.color('blue')
        elif (2 == col):
            turtle.color('green')
        elif (3 == col):
            turtle.color('purple')
        elif (4 == col):
            turtle.color('yellow')
        
        # sel로 뭘 그릴지 랜덤하게 고르기. 이 때 테두리 (또는 원 내부의) 색깔은 col로 위에서 정해졌던 랜덤 값이다.
        sel = random.randint(0, 4)
        if (0 == sel):
            turtle.forward(random.randint(50, 100)) # sel == 0일 경우, 랜덤 길이만큼 앞으로 선 그리기
        elif (1 == sel):
            turtle.right(random.randint(90, 360)) # sel == 1일 경우, 랜덤 각도만큼 오른쪽으로 돌기
        elif (2 == sel):
            turtle.begin_fill()
            turtle.circle(random.randint(-100, -20)) # sel == 2일 경우, 랜덤 크기의 색깔이 채워진 원을 오른쪽으로 그리기.
            turtle.end_fill()
        elif (3 == sel):
            turtle.forward(random.randint(30, 50)) # sel == 3일 경우, 랜덤 길이만큼 앞으로 선 그리기. sel==0일 때보다 짧은 선이다.
        elif (4 == sel):
            turtle.circle(random.randint(20, 100)) # sel == 4일 경우, 랜덤 크기의 빈 원을 왼쪽으로 그리기.
            
    
    # 이 밑 3줄(새로운 도형을 그리기 전에 새 점으로 가는 것)은 i 쓰는 for문으로 인해서 10번 반복된다.
    a = float(random.randint(-300, 300))
    b = float(random.randint(-300, 300))
    turtle.goto(a, b)


# ## 장미 그리기

# In[ ]:


import turtle as t

t.bgcolor('black')
t.color('pink') # 희한하게 여기서 t.color도 되고, t.pencolor도 된다.
t.speed(0) # 그려지는 속도. 0은 최고 속도, 1(느림) - 10(빠름)

for i in range(200):
    t.pensize(i/50) #선의 크기(굵기)
    t.forward(i) #변의 길이 i로 계속 커지게 해야 멋진 꽃이 되지.
    t.left(65) #이 숫자를 크게 줄수록 꽃잎이 뾰족해진다. 직접 해 봐라!


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




