import re

# Open the files
a = open('C:/Users/jsbjs/Desktop/코딩코/a.txt', 'r', encoding='UTF-8')
b = open('C:/Users/jsbjs/Desktop/코딩코/b.txt', 'r', encoding='UTF-8')

# Read the lines from the files
a_lines = a.readlines()
b_lines = b.readlines()

i = 0
keywords = re.findall(r'\w+', b_lines[i])

while i < len(a_lines):
    words = re.findall(r'\w+', a_lines[i])
    chars = re.findall(r'\W+', a_lines[i])

    print('\n\n')
    if re.match('\w', a_lines[i][0]):
        for j in range(len(words)):
            if words[j] in keywords:
                print('___', end = '')
            else:
                print(words[j], end = '')
            if j < len(chars):
                print(chars[j], end = '')
    else:
        for j in range(len(chars)):
            print(chars[j], end = '')
            if j < len(words):
                if words[j] in keywords:
                    print('___', end = '')
                else:
                    print(words[j], end = '')
    if j == len(a_lines) - 1:
        print('\n', end = '')
    guess = input('\n\n\nMake a guess: ')

    if guess in keywords:
        keywords.remove(guess)
        if len(keywords) == 0:
            print('\n\n' + a_lines[i], end = '')
            if i == len(a_lines) - 1:
                print('\n', end = '')
            print(f'\n\n[Line {i + 1} of {len(a_lines)} complete]', end = '')
            i += 1
            if i < len(a_lines):
                keywords = re.findall(r'\w+', b_lines[i])
    else:
        print('\n\nTry again.', end = '')

# Close the files
a.close()
b.close()