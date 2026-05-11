# a = "봄"
# b = "여름"
# print(a, b, sep="과 ", end=" 끝")
# sep: 변수 사이에 들어가는 것을 나타냄

# c = int(input("숫자 입력: "))
# for i in range(1, 10) :
    
#     print(f"{c} x {i} = {c*i}")

import time


for i in range(2, 10) :

    print(f"{i}단")

    for j in range(1, 10) :

        print(f"{i} x {j} = {i*j}", end="\t")
    print()

for i in range(10, -1, -1) :

    print(i)
    time.sleep(1)
print("발사")