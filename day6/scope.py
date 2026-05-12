def calc(r1):
    
    result = 3.14*r1**2 # r1 반지름
    
    return result

r= float(input("원의 반지름 입력: "))

area = calc(r)
print(area)
# print(result) result는 지역 변수(함수가 종료되면 소멸)

def calc2(r2):
    
    global a
    a = 3.14*r2**2 # r1 반지름
    
    return a

a = 0 # 전역 변수
rr= float(input("원의 반지름 입력: "))

calc2(rr)
print(a)