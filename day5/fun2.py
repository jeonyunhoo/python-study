# 디폴트 인수 : 함수의 매개변수가 기본값을 갖고 있을 수 있음
def greet(name, msg = "니 별 일 있나?") :

    print(f"안녕 {name}! {msg}")

greet("홍길동")

####################################

def print_star(n = 1):
    print("n =", n)

    for i in range(n) :

        print("**********************")

print_star()
print()
print_star(3) # 인수를 보내며 호출