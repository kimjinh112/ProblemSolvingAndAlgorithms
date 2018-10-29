def add10 (score):                  #return 해도, print로 끝내도 상관없습니다.     
    for i in range(len(score)):
        score[i] = score[i] + 10



def add10_not_exceed_100(score):    # 100점을 넘기지 않도록 짜고 싶은 경우
    for i in range(len(score)):
        score[i] =  min(100, score[i] + 10)

scores = [90, 25, 67, 45, 80]


add10(scores)
print(scores)


scores2 = [25, 76, 92, 88, 96, 100]
add10_not_exceed_100(scores2)
print(scores2)
