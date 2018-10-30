import random



def game():             #직관적 코딩
    
    choice = ['가위', '바위', '보']
    m = int(input('선택해주세요. (0. 가위 1.바위, 2.보) : '))
    c = random.randint(0, 2)

    me = choice[m]
    computer = choice[c]

    print()
    print('나: ', me)
    print('상대방: ', computer)
    
    game_result = ['draw', 'win', 'lose']
    
    #result win: 1      draw:0,     lose: 2
    
    if me == '가위':
        if computer == '가위':
            result = 0
        elif computer == '바위':
            result = 2
        else:
            result = 1
            
    elif me == '바위':
        if computer == '가위':
            result = 1
        elif computer == '바위':
            result = 0
        else:
            result = 2
    else:
        if computer == '가위':
            result = 2
        elif computer == '바위':
            result = 1
        else:
            result = 0
            
    print(game_result[result],'\n')


game()
    
def game_short_coding():            #짧게 줄이고 싶다.

    choice = ['가위', '바위', '보']
    m = int(input('선택해주세요. (0. 가위 1.바위, 2.보) : '))
    c = random.randint(0, 2)

    me = choice[m]
    computer = choice[c]

    print()
    print('나: ', me)
    print('상대방: ', computer)
    
    game_result = ['draw', 'win', 'lose']
    
    if m == c:          #둘이 같은 패를 냈다.           -> 비겼다.
        result = 0
        
    elif (m+1) % 3 == c:        #상대방(c)이 나의 바로 다음(m+1) 패를 냈다. -> 졌다
        result = 2
        
    elif (m-1) % 3 == c:        #상대방(c)이 나의 바로 이전(m-1) 패를 냈다 -> 이겼다.
        result = 1

                                # ' % 3' 은 3이상의 수를 [0, 1, 2] 범위로 순환시키기 위한 코드입니다.

    print(game_result[result])


game_short_coding()
