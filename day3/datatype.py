# 리스트

subway = ['아이유', '변우석', '박지훈', '유재석']
print(subway)

subway.append('장원영') #추가
print(subway)

subway.insert(1, '카리나') #원하는 위치에 추가
print(subway)

print(subway.index("박지훈")) # 위치 확인

print(subway.pop())
print(subway)

name = subway.pop(1)
print(name)

subway.remove('유재석')
print(subway)

subway.append('아이유')
print(subway)

print(subway.count('아이유')) # 아이유가 몇 명 있는지

subway.remove('아이유') # 아이유 제거
print(subway)

num_list = [5, 2, 4, 3, 1]
print(num_list)

num_list.sort() # 오름차순 정렬
print(num_list)

num_list.reverse() # 내림차순 정렬
print(num_list)

num_list.clear() # 리스트 모두 제거
print(num_list)

# 튜플: 순서있음, 나열형, 수정 불가능

menu = ("김밥", "오뎅")
print(menu)
# menu[1] = "피자" #튜플은 수정 불가능
print(menu)

(name, age, addr) = ("이순신", 30, "안산")
print(name, age, addr)

# classroom = (407: "개발자 과정", 402: "영상 과정")
classroom = {407: "개발자 과정", 402: "영상 과정"}
print(classroom)
print(classroom[407])
# print(classroom[404]) # 없는 키는 오류 발생

print(classroom.get(407))
print(classroom.get(404)) # 없는 키는 None 반환

print(classroom.keys()) # 키
print(classroom.values()) # 값
print(classroom.items()) # 키와 값 쌍

del classroom[402] # 키 402 제거
print(classroom)