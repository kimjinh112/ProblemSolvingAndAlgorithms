class Dog:
    def __init__(self, Name, Color, Kind):
        self.name = Name
        self.color = Color
        self.kind = Kind

    def sit(self):
        print('앉았습니다')

    def lay(self):
        print('엎드립니다.')

    def tail_whip(self):
        print('살랑 살랑~')

    def bark(self):
        print('왈왈~!')


sensation = Dog('센세이션', 'black', '요크셔테리어')
sensation.sit()
sensation.lay()
sensation.tail_whip()
sensation.bark()
