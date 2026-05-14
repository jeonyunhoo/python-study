class Passbook:
    
    def __init__(self, owner, balance):
        
        self.owner = owner
        self.balance = balance

    def deposit(self, plus_m):
        
        self.balance += plus_m
        print(f"입금액: {plus_m}    잔액: {self.balance}")
        
    def withdraw(self, dis_m):
        
        if self.balance < dis_m:
            
            print("잔액 부족")
        else:
            
            self.balance -= dis_m
            print(f"출금: {dis_m}   잔액: {self.balance}")
            
    def showInfo(self):
        
        print(f"예금주: {self.owner}    잔액: {self.balance}")
        
class MinusPassbook(Passbook):
     
    def withdraw(self, dis_m):
        
        if self.balance < dis_m:
            
            if (self.balance - dis_m) < -1000000:
                
                print("마이너스 한도 초과")
            else:
                
                self.balance -= dis_m
                print(f"출금: {dis_m}   잔액: {self.balance}")
        else:
            
            self.balance -= dis_m
            print(f"출금: {dis_m}   잔액: {self.balance}")
            
account1 = Passbook("홍길동", 100000)

account1.withdraw(50000) 
account1.withdraw(120000)

account2 = MinusPassbook("김철수", 100000)
account2.withdraw(120000) # 자식 클래스 호출
account2.withdraw(9000000)