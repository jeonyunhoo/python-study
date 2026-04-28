import turtle
import random

t = turtle.Turtle() # turtle 객체 생성, t 변수에 할당
turtle.colormode(255)

t.speed(20)

t.shape("arrow") # 거북이 모양으로 설정

radius = 50 # radius 변수에 정수형 50 설정
t.circle(radius) # turtle이 그릴 원의 반지름의 길으를 50으로 설정

t.fd(30) #앞으로 이동
t.circle(radius)

for _ in range(4):

    t.fd(2 * radius)
    t.right(90) # 전진과 직각 방향 전환을 반복하여 정사각형을 그림

for _ in range(3):

    t.backward(2 * radius)
    t.right(120) # 전진과 120도 우측 방향 전환으로 정 삼각형을 그림

t.fd(3 *radius)

a = 0

for _ in range(100000):

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    t.pencolor(r, g, b)

    t.circle(a)
    a += 10
