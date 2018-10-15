num = int(input('1 이상의 정수 입력: '))

Divisor = []

for i in range(1, num+1):
    if num % i == 0:
        Divisor.append(i)
    
print(num,'의 약수는')

for i in Divisor:
    print(i)
