'''
Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j)
such that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2.
'''

def solution(numbers):
    count=0
    for i in range(0,len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i] <= numbers[j]:
                tempSum = numbers[i] + numbers[j]
                if (tempSum != 0) and (tempSum & (tempSum-1) == 0):
                    print(tempSum)
                    count+=1
    return count
def powerOfTwo(num):
    return(num!=0) and (num & (num-1) == 0)
print(solution([1,-1,2,3]))
#print(solution([2]))