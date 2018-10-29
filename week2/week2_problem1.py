'''
1. 나이를 자연수의 형태로 입력을 받는다.

2. 나이가 20 이상이라면 'you are an adult' 출력

3. 2의 경우에 해당하지 않으면서 나이가 10살 이상이면 'you are an adolescent' 출력

4. 이외에는 'you are a baby'를 출력한다.

(0보다 작은 입력은 생각하지 않겠음)

'''


age = int(input('나이를 입력하세요: '))

if age >= 20:
    print('you are an adult')
elif age >= 10:
    print('you are an adolescent')
else:
    print('you are a baby')

