class Board:
    
    def set_data(self, title, writer): # 책 제목, 저자 저장
        
        self.title = title # java의 'this'를 python에서는 'self'를 사용한다.
                           # 우측 title은 호출시 받아온 매개 변수값
                           # 좌측 title은 객체의 멤버 변수
        self.writer = writer
        self.cnt = 0
        
    def cntup(self): # 조회수를 구하는 함수
        
        self.cnt += 1

# Board board1 = new Board(), java 방식
board1 = Board() # python # 객체 변수 = 클래스(매개 변수)
board2 = Board()

board1.set_data("파이썬의 정석", "파2썬")
board2.set_data("자바의 정석", "잡아")

board1.cntup()
board1.cntup()
board2.cntup()

print(f"책 제목: {board1.title}, 저자: {board1.writer}, 호출 횟수: {board1.cnt}")
print(f"책 제목: {board2.title}, 저자: {board2.writer}, 호출 횟수: {board2.cnt}")

board3 = Board()
# board3.cntup() # 오류 set_data를 미리 불러오지 않아 'cnt'변수가 생성되지 않음
board3.set_data()
board3.cntup()