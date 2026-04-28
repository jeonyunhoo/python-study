product = input("상품의 이름을 입력해주세요: ")
price = int(input("상품의 가격을 입력해주세요: "))
cnt = int(input("상품의 개수를 입력해주세요: "))

pay = price * cnt

print(product, "의 총 금액은 ", pay, "원 입니다.")
# print(product + "의 총 금액은 " + pay + "원 입니다.")
#                            숫자와 문자 사이 '+'기호 사용 불가능
# print(product + "의 총 금액은 " + str(pay) + "원 입니다.")
#                             pay를 문자형으로 변환. '+' 사용 가능
# print(f"{product}의 총 가격은 {pay}입니다.")
#f-string: 포맷 문자열 ==> 변수는 {}안에 작성