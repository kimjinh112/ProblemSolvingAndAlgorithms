import random

def shell(alist):
    interval = len(alist)//2
    while interval > 0 :
        gapInsertionSort(alist, interval)
        interval//= 2

def gapInsertionSort(alist, interval):

    for index in range(len(alist)):
        position = index
        cur_Value = alist[index]

        while (position >= interval ) and alist[position - interval] > cur_Value:
            alist[position] = alist[position - interval]
            position -= interval
        alist[position] = cur_Value


dataset = []
for a in range(15):
    dataset.append(random.randint(1,50))
print("Before shellsort:")
print(dataset)
print("After shellsort:")
shell(dataset)
print(dataset)

'''
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before shellsort:")
print(alist)
print("After shellsort:")
shell(alist)
print(alist)

'''
