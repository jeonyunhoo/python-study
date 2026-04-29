mony = int(input("투입한 돈: "))
obj_price = int(input("물건의 가격: "))

if mony < obj_price:

    print("돈이 부족합니다.")

else:

    change = mony - obj_price
    charge_500 = change // 500
    charge_100 = (change % 500) // 100
    print(f"거스름돈: {change}원")
    print(f"500원 동전의 개수: {charge_500}개")
    print(f"100원 동전의 개수: {charge_100}개")