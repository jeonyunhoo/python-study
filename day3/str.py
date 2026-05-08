# 문자열
s = "Hello python!"
print(s[6]) # 인덱싱
print(s[6:12]) # 슬라이싱

jumin = "080120-3234567"
print("성별: " + jumin[7])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("뒷자리: " + jumin[7:])
print("뒷자리: " + jumin[-7:])

s1 = "나는 학생입니다."
s2 = "나는 파이썬을 배웁니다."
s3 = '재밌습니다.' # 작은 따옴표로도 문자열을 만들 수 있다.

s4 = """ # 여러 줄 문자열, 입력한 그대로 저장

나는 학생입니다.
나는 파이썬을 배웁니다.
재밌습니다.
"""
print(s4)

year = "1977"
month = "11"
day = "29"
date = year + "-" + month + "-" + day
print(date)

date2 = date.split("-") # 문자열을 특정 구분자로 나누어 리스트로 반환
print(date2)
print(type(date2))
print(date2[1][0:2], end = "*")

name = "kakao taxi"
name2 = name.replace("k", "t", 1)
print(name2)

print("python"*5)

won = "63,120,450"
won2 = won.replace(",", "")
print(won2)

won3 = 345908800
won4 = format(won3, ",d")
print(won4)

p = "Python is Amazing"
print(p.lower()) # 소문자
print(p.upper()) # 대문자
print(p.capitalize()) # 첫 글자 대문자
print(p[0].isupper()) # 대문자인지 확인
print(len(p)) # 문자열 길이
print(p.count("i")) # 문자열 내 특정 문자 개수

# 위치
index = p.find("i")
print(index)
index = p.index("i", index + 1) # 14
print(index)

words = ["Python", "is", "easy"]
result = " ".join(words) #" " 사이에 공백을 넣으며 연결
print(result)

text = "   Hello       Python!   ****"
print(text.strip()) # 공백 제거
print(text.rstrip("*"))

num = "5"
result = num.zfill(3) # 3자리로 만들고 빈 공간은 0으로 채움
print(result)

age = 19
print("나는 %d살입니다" % age) # %d는 정수, %s는 문자열, %f는 실수
print("나는 {}살입니다".format(age)) # {}는 format에서 값을 넣을 위치를 나타냄

like = "노래부르기"
print("나는 %d살이고 %s를 좋아합니다." % (age, like))
print("나는 {0}살이고 {1}를 좋아합니다.".format(age, like))
print(f"나는 {age}살이고 {like}를 좋아합니다.")

print("나의 주소는 {addr}이며, 나의 키는 {height}cm입니다.".format(addr = "인천", height = 165))

print("\n배우는 과목은\n \"파이썬\" 입니다")
# \r: 커서를 맨 앞으로 이동
print("red   apple\rpine")
print("i like you\b!!") # \b: 한 글자 삭제
print("red\t apple") # \t: 탭

print(p.find("A")) # 찾는 문자가 없으면 -1 반환
print(p.rfind("A")) # 오른쪽 부터 찾음
print(p.index("a")) # 찾는 문자가 없으면 -1 반환
print(p.rindex("a")) # 오른쪽 부터

print(p.find("java")) # 찾는 문자가 없으면 -1 반환
# print(p.index("java")) # 찾는 문자가 없으면 오류 발생

arr_Str = input("Input String: ").split("-")
# inforrmation-technology -> '-'을 기준으로 나누어 저장 [0][1]
arr_Len = int(input("Input Number: ")) # 12
arr_Val = list(range(0, arr_Len, 2)) # 0부터 arr_Len까지 2씩 증가하는 숫자 리스트 [0, 2, 4, 6, 8, 10]
arr_Val.remove(4) # 4라는 값 제거

print(arr_Str[1].find('i') + arr_Val[2])
# technology에서 i를 찾음 -> find 할 때 없으면 -1
# -1 + arr_Val[2] -> 6 = 5