num = int(input("3의 배수 입력: "))
num2 = int(input("5의 배수 입력: "))


match num % 3, num2 % 5:

    case 0, 0:

        print("num은 3의 배수 num2는 5의 배수")
    case 0, _:

        print("num은 3의 배수 num2는 아무숫자")
    case _, 0:

        print("num은 아무숫자 num2는 5의 배수")
    case _:

        print("오류")