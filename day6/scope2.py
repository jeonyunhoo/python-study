#파이썬은 변수를 찾을 때 가장 가까운 영역부터 찾음
# LEGB 규칙 (Local -> Enclosing -> Global -> Built-in)
# Local -> 함수 내부 변수
# enclosing -> 바깥 함수 변수
# Global -> 함수 밖 변수
# Built-in -> Python이 기본 제공하는 이름(print, input, len...)
a = '홍길동' # 전역 변수
b = 99

def function1():
    a = '이순신' # 중첩 함수
    c = [1 ,2 ,3]
    
    def function2():
        d = (1, 2, 3) # 지역 변수
        print('Local a =',a) # 이순신 
        print('Local b =',b) # 99
        print('Local c =',c) # [1, 2, 3]
        print('Local d =',d) # (1, 2, 3)

    function2()
    print('Enclosing a =',a) # 이순신
    print('Enclosing b =',b) # 99
    print('Enclosing c =',c) # [1, 2, 3]
    # print('Enclosing d =',d) # x
    
function1()
print('Global a =',a) # 홍길동
print('Global b =',b) # 99
# print('Global c =',c) # x 
# print('Global d =',d) # x