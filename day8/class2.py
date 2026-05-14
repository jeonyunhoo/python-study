class Board:
    
    def __init__(self, title, writer): #python은 init이라 써놓으면 알아서 생성자로 인식
        
        self.title = title
        self.writer = writer
        
        self.cnt = 0
        
    def cntup(self):
        
        self.cnt =+ 1
        
board1 = Board("자바의 정석", "잡아")
board2 = Board("파이썬의 정석", "파2썬")

board1.cntup()
board1.cntup()
board2.cntup()

print(f"책 제목: {board1.title}, 저자: {board1.writer}, 호출 횟수: {board1.cnt}")
print(f"책 제목: {board2.title}, 저자: {board2.writer}, 호출 횟수: {board2.cnt}")
