fruits = ["사과", "배", "오렌지"]

try:
    
    index = int(input("번호를 입력하세요(0/1/2): "))
    if index < 0 or index >= len(fruits):
        raise IndexError # 예외를 발생시킴+        
except IndexError:
            
        print("없는 인덱스 입니다.")
except ValueError:
    
    print("잘못 입력하셨습니다.")
except Exception as e:
    
    print("오류입니다: ", e)
else:
    
    print(fruits[index])
finally:
    
    print("종료합니다.")