def solution(s1,s2):
    tempDict = {}
    tempDict1 = {}
    returnStr = ''
    for char in range(len(s1)):
        if s1[char] not in tempDict:
            tempDict[s1[char]] = 1
        else:
            tempDict[s1[char]] += 1

    for char in range(len(s2)):
        if s2[char] not in tempDict1:
            tempDict1[s2[char]] = 1
        else:
            tempDict1[s2[char]] += 1
    # print(tempDict)
    # print(tempDict1)

    l1 = list(s1)
    l2 = list(s2)
    result = []
    print(l1, "vs.", l2)
    while l1 and l2:
        print(l1, " <----> ", l2, "      result:", result)
        if tempDict[l1[0]] < tempDict1[l2[0]]:
            result.append(l1.pop(0))
        elif tempDict1[l2[0]] < tempDict[l1[0]]:
            result.append(l2.pop(0))
        else:
            if l1[0] <= l2[0]:
                result.append(l1.pop(0))
            else:
                result.append(l2.pop(0))

    while l1:
        result.append(l1.pop(0))

    while l2:
        result.append(l2.pop(0))

    print("after", l1)
    print("after", l2)



    return result


# print(solution('super', 'tower'))
print(solution('dce', 'cccbd'))
# result = []
# left = [d, c, e]
# right = [c, c, c, b, d]
# 1st. compare d vs. c
# remove left

# result = [d]
# left = [c, e]
# right = [c, c, c, b, d]