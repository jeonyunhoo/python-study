# for i in range(6):
#0~5까지 6번 반복

# 딕셔너리: 키와 값으로 구성
# snack = {

#     "새우깡":3000,
#     "감자깡":3500,
#     "양파링":4000
# }

# for i in snack:

#     print(i) #키값이 출력됨
# print()

# for j in snack.values():

#     print(j) #값이 출력됨
# print()

# for j in snack.items():

#     print(j) #키와 값이 튜플로 출력됨

# 리스트

fruit = ["파인애플", "참외", "배", "오랜지", "드래곤 후르츠"]
cart = []
for i in fruit:

    if(len(i) <= 3):

        cart.append(i)
print(cart)