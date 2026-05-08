# set(집합)
# set은 중복을 허용하지 않고 순서가 없다.
# {}, set ( {} )

my_set = {"홍길동", "김길동", "장길동"}
print(my_set)

football = {"홍길동", "김길동", "장길동"}
# baseball = {"홍길동", "오길동", "정길동"}
baseball = set(["홍길동", "오길동", "정길동"])

print(football | baseball) # 합집합
print(football.union(baseball)) # 합집합

print(football & baseball) # 교집합
print(football.intersection(baseball)) # 교집합

print(football.difference(baseball)) # 차집합
print(football.symmetric_difference(baseball)) # 대칭 차집합

# 추가
football.add("성길동")
print(football)

# 삭제
football.remove("홍길동")
print(football)

spo1 = list(baseball)
print(type(spo1))

spo2 = tuple(baseball)
print(type(spo2))
