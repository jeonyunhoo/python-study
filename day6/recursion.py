# 재귀 호출
# 5!(팩토리얼): 1~5까지 곱함
# def fact(n): #fact 함수 (매개 변수는 1개)
    
#     if n == 1:
        
#         return 1
#     else:
#         return n * fact(n-1) # 5 x fact(4) = 5 x (4 x fact(3)) 이하 동일
    
# a = int(input("정수를 입력해주세요: "))
# res = fact(a) # 함수 호출, 인수 a(정수) 보냄
# 반환되어 온 결과값을 res에 저장
# print(f"{a}!은 {res} 이다")

def fac(n):
    
    if n == 1:
        
        return 1
    else:
        
        return n + fac(n-1)
    
b = int(input("정수를 입력하세요: "))
las = fac(b)
print(f"{las}입니다.")

