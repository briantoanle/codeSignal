temp = commands[shortcut]

if temp not in dict1 and (temp == 'ls' or temp == 'cp' or temp == 'mv'):
    dict1[commands[shortcut]] = 1
elif '!' in temp:
    print(temp, "temp")
    count = 0
    # print(commands[int(temp[-1])],'lalala')
else:
    dict1[commands[shortcut]] += 1


# ['ls','cp','mv','!1','!2','!3']


# [1,3,2]