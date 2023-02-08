s = "ab12c"
t = "ab24z"
#test function
def solution1(s,t):
    count = 0
    print(s)
    print(t)
    ls = list(s)
    lt = list(t)
    print(ls)
    print(lt)

    countdigits = 0
    for i in range(len(s)):
        if s[i].isdigit():
            countdigits +=1

    while countdigits != 0:
        s1 = s
        for i in range(len(s1)):
            if s1[i].isdigit():
                s1.replace(s1[i],'asd')
                print('s1',s1)
            if t > s1:
                count+=1
        countdigits -=1

    countdigitt= 0
    for i in range(len(t)):
        if t[i].isdigit():
            countdigitt +=1
    while countdigitt != 0:
        t1= t
        for i in range(len(t1)):
            if t1[i].isdigit():
                t1.replace(t1[i],"",1)
        if t1 > s:
            count+=1
        countdigitt -=1
    print('count ', count)

def solution(s, t):
    print(s)
    print(t)
    counter = 0
    for i in range(len(s)):
        if s[i].isdigit():
            temp = s[:i] + s[i+1:]
            if temp <= t:
                counter += 1
    for i in range(len(t)):
        if t[i].isdigit():
            temp = t[:i] + t[i+1:]
            if temp >= s:
                counter += 1
    return counter
print(solution(s,t))