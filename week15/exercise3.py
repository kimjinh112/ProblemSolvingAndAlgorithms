
# 클래스 속성 정의
class Book:
    title = ""
    publisher = ""
    author = ""

    def __init__(self):
        print('init')
        super().__init__()
        
# 클래스 내부 기능 정의

    def setdata(self, title, publisher, author): 
        self.title = title
        self.publisher = publisher
        self.author = author

    def getdata(self):
        print("책 제목: ", self.title)
        print("출판사: ", self.publisher)
        print("저자: ", self.author)
    
#인스턴스 생성 및 사용
obj = Book()
t = input("책 제목 입력: ")
p = input("출판사 명 입력: ")
a = input("저자 명 입력: ")

obj.setdata(t, p, a)
obj.getdata()
