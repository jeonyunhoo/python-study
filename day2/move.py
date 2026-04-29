movie_list = ["아바타", "해리포터", "살목지", "마이클"]
print(movie_list)

movie_list.insert(1, "범죄도시") #삽입
print(movie_list)

movie_list.append("탑건") #추가
print(movie_list)

movie_list.remove("살목지") #값을 지정하여 삭제
print(movie_list)

#del: 명령어
del movie_list[2]
print(movie_list) #요소 위치 지정 삭제

x = 10
print(x)
del x
#print(x)

print(len(movie_list)) #len: 길이

a= [1, 2, 3]
print(len(a))

# 90, 50, 80, 70, 55

b = [90, 50, 80, 70, 55]
sum = b[0] + b[1] + b[2] + b[3] + b[4]
d = int(sum / len(b))
print(f"평균 {d}")