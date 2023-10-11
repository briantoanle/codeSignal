
# given a string s consisting of small english letters
# find and return the first instance of a non-repeating character in it
# if there is no such character, return '_'
def solution(s):

    # make an array with 26 values
    arr = [0] * 26
    dictionary = {}
    for i in s:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] +=1
    #print(dictionary)
    for key in dictionary:
        if dictionary[key] == 1:
            return key
    return "_"
    '''for i in s:
        arr[ord(i)-97] += 1
    print(arr)
    for i in range(len(arr)):
        if arr[i] == 1:
            return chr(i+97)
    return "_"'''

print(solution("ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof"))