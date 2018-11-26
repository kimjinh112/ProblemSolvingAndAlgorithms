class Tv:

    def __init__(self, vol = 10, ch = 11, color = 'black'):     #class 선언시 self는 반드시 주셔야 합니다.  (반드시 '_' 2개!)
                                                                #클래스 생성 시 인자를 안 줄 때의 기본 인자 값 설정
        print('TV를 생성합니다.')
        self.power = False                                      # self.power를 사용하면 다른 함수 내에서도 이 변수를 사용할 수 있다.
        self.vol = vol                                          # self는 객체가 변수를 소유할수 있도록 만든다.
        self.ch = ch
        self.color = color

    def Turn_on(self):
    # self.power라는 변수를 처음 보지만 사용할 수 있다.
        if not self.power:                                      
            print('TV를 켭니다.')
            self.power= True
        else:
            print('Tv가 이미 켜져 있습니다.')

    def Turn_off(self):

    # self.power라는 변수를 처음 보지만 사용할 수 있다.
        if self.power:                                      
            print('TV를 켭니다.')
            self.power= False
        else:
            print('Tv가 이미 꺼져 있습니다.')

    def vol_up(self, v = 1):

    # Tv를 켰을 때만 동작하도록
        if self.power:                                      

        # 볼륨을 높일 수 없는 경우 바로 종료
            if self.vol == 100:                             
                print('이미 최대 볼륨입니다')
                return
            
            print('볼륨을 ', v ,'만큼 높입니다.') 
            self.vol += v
            self.vol = min(self.vol, 100)                   #volume은 100을 넘기지 않게 구현할 경우

    def vol_down(self, v = 1):
        if self.vol == 0:
            print('음소거 상태입니다.')
            return

        print('볼륨을 ', v ,'만큼 낮춥니다.') 
        self.vol -= v
        self.vol = max(self.vol, 0)                         #volume이 음수가 되지 않게 함.


    def change_channel(self, ch):

    # 채널이 1~999까지만 있을때의 예시
        if ch < 0 or ch >= 1000:
            print('올바르지 않은 채널 값입니다')            
            return

        print(ch, '번 채널로 변경합니다')
        self.ch = ch
        
my_Tv = Tv()                                                # vol = 10, 채널은 11, 색상은 black으로 자동 설정
your_Tv = Tv(10, 8, 'silver')                               # vol = 10, 채널은 8, 색상은 은색
new_Tv = Tv(ch = 4, vol = 5)                                # 인자 순서를 무시하고 직접 줄 수도 있다.

#Turn_off 함수는 인자로 self를 요구하나 self는 사실 자동으로 전달된다.
#즉, 인자 없이 호출 가능하다.
my_Tv.Turn_off()                                            # Tv는 원래 꺼져 있는 상태
my_Tv.vol_up()


my_Tv.Turn_on()

#역시 self는 자동으로 전달 되므로 vol 인자만 주어도 호출이 가능하다.
my_Tv.vol_up(5) 
my_Tv.change_channel(20)

            
