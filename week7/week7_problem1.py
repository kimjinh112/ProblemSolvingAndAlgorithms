def Total(listA):           # 여기는 Total의 함수 영역입니다.
    Sum = 0                 # 여기서는 전달받은 매개변수를 listA라고 부르기로 했습니다. (받을 때의 이름은 score지만 여기서는 listA라고 부르기로 합니다.)
    for s in listA:         # 
        Sum += s            # 여기 라인은 for문의 영역으로 반복할 코드만 작성합니다
    return Sum              # return 할때 들여쓰기 주의! 이 상태에서 Tab 한 번 더 할시 return문이 for문 내부 명령어로 인식되어 for문이 한번만 실행되고 Sum을 바로 반환하게됨


def Avg(listA):
    n = len(listA)
    average = int(Total(listA) / n)

    return average

def Max(listA):

    maximum = listA[0]
    for s in listA:
        if maximum < s:
            maximum = s

    return maximum

score = [90, 80, 70, 60, 50]

total = Total(score)            
avg = Avg(score)
maximum = Max(score)

#total = sum(score)
#avg = total/len(score)
#maximum = max(score)

print('총점 점수: ', Total(score))
print('평균 점수: ', Avg(score))
print('최대 점수: ', Max(score))
