
string1 = "aabcc"
string2 = "adcaa"
common_chars = ""
for char1 in string1:
    for char2 in string2:
        if char1 == char2:
            common_chars += char1
print(common_chars)


