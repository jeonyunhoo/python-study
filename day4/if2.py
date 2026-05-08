# num = int(input("주민 번호 입력: ")).split("-")

# if num[1][0] == "1" or num[1][0] == "3" :
#     print("남자")
# elif num[1][0] == "2" or num[1][0] == "4" :
#     print("여자")
# else :
#     print("잘못된 주민 번호입니다.")

# if num[7] == "1" or num[7] == "3" :
#     print("남자")
# elif num[7] == "2" or num[7] == "4" :
#     print("여자")
# else :    
#     print("잘못된 주민 번호입니다.")

num1, num2, num3 = map(int, input("숫자 세 개 입력: ").split())

if num1 > num2 and num1 > num3 :
    print(num1)
elif num2 > num1 and num2 > num3 :
    print(num2)
else :
    print(num3)