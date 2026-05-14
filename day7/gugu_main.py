# from gugu_modul import *
import gugu_modul

while True:
    
    ans = int(input("숫자를 입력해 주세요(1/2/0(종료)): "))
    
    if ans == 0:
        
        break
    elif ans == 1:
        
        # v_gugudan()
        gugu_modul.v_gugudan()
    elif ans == 2:
        
        # h_gugudan()
        gugu_modul.h_gugudan()
        print()
    else:
        
        print("다시 입력")