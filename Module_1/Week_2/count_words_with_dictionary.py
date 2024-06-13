def count_chars(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


str = 'Happiness'
str_2 = 'smiles'

print(count_chars(str))
print(count_chars(str_2))
