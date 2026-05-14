try: # 수행 문장 내에서 에러가 난다면 어떤 시퀀스를 취할지 정함
    
    num = int(input("숫자 입력: "))
    res = 10 / num
except ValueError: # 문자 입력시
    
    print("숫자가 아닙니다.")
except ZeroDivisionError: # 0 입력시
    
    print("0으로 나눌 수 없습니다.")
except Exception as e: # 나머지 에러들 e변수에 예외 저장
    
    print("에러메시지: ", e)
finally: # 공통적 수행(무조건 수행)
    
    print("종료합니다.")    