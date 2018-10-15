goodsay = ['happy', 'love', 'sad', 'hot', 'angry', 'fortunate']

num = int(input('0~5의 숫자를 입력해주세요: '))

while num < 0 or num > 5:                                     #필수 코드 아님
    print('입력이 잘 못 되었습니다.')                         #
    num = int(input('0~5의 숫자를 입력해주세요: '))           #

print(goodsay[num])
