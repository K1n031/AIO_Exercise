def word_count(file_path):
    word_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().lower()
            words = line.split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    return word_dict

file_path = 'Data/P1_data.txt'
print(word_count(file_path))