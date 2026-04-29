am_price = 2000
cp_price = 3000
capu_price = 3500

a = int(input("아메리카노의 개수를 입력해주세요: "))
c = int(input("카페라떼의 개수를 입력해주세요: "))
p = int(input("카푸치노의 개수를 입력해주세요: "))

pay = (am_price * a) + (cp_price * c) + (capu_price * p)
print(f"총 매출은 {pay}원 입니다.")