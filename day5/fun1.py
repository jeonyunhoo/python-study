#함수

# def add(i, j) :
    
#     return i + j


# n1 = int(input("첫 번째 숫자 입력 : "))
# n2 = int(input("두 번째 숫자 입력 : "))

# sum = add(n1, n2)
# print(sum)

###############################


def avg(score_list) :
    
    return sum(score_list) / len(score_list)

score_list = [80, 90, 100, 50, 20]

sum = avg(score_list)
print(sum)