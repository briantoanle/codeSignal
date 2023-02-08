'''
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array.
Return the array of these digits in ascending order.
'''

def solution(a):
    temp = ''
    temp = ''.join(map(str,a))
    print(temp)
    arr = [0,1,2,3,4,5,6,7,8,9]
    for i in range(10):

        arr[i] = temp.count(str(i))
    print(arr)
    maxnum = max(arr)
    returnArr = []
    for i in range(10):
        if arr[i] == maxnum:
            returnArr.append(i)

    returnArr.sort()
    return returnArr
print(solution([25,2,3,57,38,41]))