num = [8, 7, 3, 2, 9, 4, 1, 6, 5]

Min = num[0]            # Min = 8로 시작
Max = num[0]            # Max = 8로 시작

for i in range(1, len(num)):            #num의 2번째 ~ 마지막 값까지만 비교
    if num[i] < Min:                    
        Min = num[i]                    #최소값 갱신
    if num[i] > Max:
        Max = num[i]                    #최대값 갱신
        
print('최대값: ', Max)
print('최소값: ', Min)
