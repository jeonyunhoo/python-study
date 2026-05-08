# str = input("영어 한 자 입력: ")

# if str.isupper() :
#     print(str.lower())
# else :
#     print(str.upper())

score = int(input("점수 입력: "))

if score > 80 :
    print("A")
elif score > 60 :
    print("B") 
elif score > 40 :
    print("C")
elif score > 20 :
    print("D")
else :
    print("E")

# if 80 < score <= 100 :
#     print("A")
# elif 60 < score <= 80 :
#     print("B")
# elif 40 < score <= 60 :
#     print("C")
# elif 20 < score <= 40 :
#     print("D")
# else :
#     print("E") # 두 방법 모두 가능하지만 첫 번째 방법이 더 간결하다.

# if score >= 81 and score <= 100 :
#     print("A")
# elif score >= 61 and score <= 80 :
#     print("B")
# elif score >= 41 and score <= 60 :
#     print("C")
# elif score >= 21 and score <= 40 :
#     print("D")
# else :
#     print("E") # 세 번째 방법도 가능하지만 첫 번째 방법이 더 간결하다.