
# 클래스 속성 정의
class Phone:
    name = ""
    tel = ""

    def __init__(self):
        print('init')
        super().__init__()
        
# 클래스 내부 기능 정의

    def setName(self, name):
        self.name = name

    def setTel(self,tel):
        self.tel = tel;

    def getName(self):
        return self.name

    def getTel(self):
        return self.tel

#인스턴스 생성 및 사용
phone1 = Phone()
phone1.setName("이재원")
phone1.setTel("010-1234-1234")
print("이름: ", phone1.getName())
print("전화번호: ", phone1.getTel())
