
# 클래스 속성 정의
class Rect:
   

    def __init__(self):
        print('init')
        super().__init__()
        
# 클래스 내부 기능 정의

    def setdata(self): 
        self.width = int(input("가로 입력: "))
        self.height = int(input("세로 입력: "))

    def area(self):
        result = self.width * self.height
        return result

#인스턴스 생성 및 사용
obj = Rect()
obj.setdata()

print("사각형의 면적은 ", obj.area())
