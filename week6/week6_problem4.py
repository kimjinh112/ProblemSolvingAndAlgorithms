
num = int(input('몇 개의 과일을 넣으시겠습니까? '))

fruits = []


for i in range(num):
    fruit = input('과일 넣기: ')
    fruits.append(fruit)
    print(fruits)

print('순서대로 과일 꺼내기: ', end=' ')

while fruits:
    print(fruits.pop(), end=', ')
    


'''
#나는 예제랑 똑같은 형식으로 출력하고 싶다

num = int(input('몇 개의 과일을 넣으시겠습니까? '))

fruits = []


for i in range(num):
    fruit = input('과일 넣기: ')
    fruits.append(fruit)

    for i in range(len(fruits)):

        if i == len(fruits) - 1:
            print(fruits[i])
        else:
            print(fruits[i], end=', ')
    
print('순서대로 과일 꺼내기: ', end=' ')

while fruits:
    if len(fruits) > 1:
        print(fruits.pop(), end=', ')
    else:
        print(fruits.pop())
        
'''
