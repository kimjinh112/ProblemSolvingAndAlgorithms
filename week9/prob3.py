def bigger5(nums):              #나는 새로운 리스트를 만들어서 반환하고 싶다.
    result = []
    for i in nums:
        if i > 5:
            result.append(i)
    return result



def bigger5_version2(nums):     #나는 원본리스트 자체에서 빼내고 싶다.

    for i in range(len(nums)-1, -1, -1):        #리스트를 거꾸로 조회하면서 삭제해야
                                                #pop시 index가 한칸씩 앞으로 당겨지는 문제 발생안합니다.
        if nums[i] <=5:
            nums.pop(i)
    return nums

a = [1, 5, 9, 10, 2, 7]


print('version1: ', bigger5(a))
print('version2: ', bigger5_version2(a))
