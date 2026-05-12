def dis_price (price, dis):

    return int(price - (price * (dis/100)))

#상품 a 할인율 10%, 책정 후 결재 금액 책정
price_a = dis_price(10000, 10)
print(f"가격: {price_a}")

price_b = dis_price(50000, 20)
print(f"가격: {price_b}")