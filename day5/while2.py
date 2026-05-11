while 1:

    a = int(input("숫자 입력: "))
    if a == 0:
        break

print("="*20)

menu = ["김밥", "라면", "떡볶이", "순대", "튀김"]
b = input("메뉴 번호 입력: ")

while b in menu:

    print(b)
    b = input("메뉴 번호 입력: ")
    #while 문장 안에서 반드시 거짓으로 변경하거나 break문을 사용해야 무한루프에 빠지지 않음

