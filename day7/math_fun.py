res = divmod(11, 3)
print(res) # 몫(//), 나머지(%) (3, 2)

print(abs(-5)) # 절대값

print(pow(4, 2)) # 제곱 '**'과 같음

print(max(10, 30, 5)) # 최대
print(min(10, 30, 5)) # 최소
print(round(23.89)) # 반올림

import math # 이처럼 작성할 시 math의 함수를 사용할 때 'math.~'과 같이 작성해야 함
# from math import * # math의 모든 함수를 name space에 가져옴 # 이처럼 작성 할 시 math의 함수를 사용할 때 'math.'을 생략하고 작성해도 됨

print(math.floor(24.9)) # 내림
print(math.ceil(23.8)) # 올림
print(math.sqrt(16)) # 제곱근
print(math.factorial(5)) # 펙토리얼
print(math.pi) # 원주율