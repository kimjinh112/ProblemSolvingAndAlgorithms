def calcTime(Time):
    if Time > (60 * 60 * 24):
        print('입력한 시간이 하루를 초과합니다')
    else:
        second = Time % 60
        Time //= 60

        minute = Time % 60
        Time //= 60

        hour = Time

        print(hour, '시간', minute, '분', second, '초')

Time = int(input('하루 이내의 초를 입력하라: '))

calcTime(Time)
        
