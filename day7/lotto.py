import random

def get_lotto():
    
    numbers = []
    while len(numbers) < 6:
        
        n = random.randint(1, 45) # 무작위 수 발생 (1 ~ 45 사이)
        
        if n not in numbers: # n에 저장된 수가 이미 numbers에 저장되어있는지 확인
            # 중복 방지
            numbers.append(n) # 추가
    return numbers # 6개의 숫자가 있는 리스트를 반환함

print(get_lotto()) # 다른 변수에 반환값을 담지 않고 호출과 출력을 동시에 함
