import re

i = 0

#파일 실행(문장) / File execution(Sentences)
a = open('Your file A goes here.', 'r', encoding='UTF-8')
a_line = a.readlines()

#파일 실행(단어) / File execution(Words)
b = open('Your file B goes here.', 'r', encoding='UTF-8')
b_line = b.readlines()

#정규표현식 한 묶음으로 / Regular expression as a group of words
pattern_words = r'\w+'
pattern_special = r'\W+'

#첫 예시 문장 출력 / The first example sentence
while i < len(a_line):
    #두 집합 중 하나에 원소 추가 / Adding elements to the two sets
    index_words = 0
    index_special = 0
    words = re.findall(pattern_words, a_line[i])
    special = re.findall(pattern_special, a_line[i])

    #전체집합 초기화 / Resetting the universal set
    combined = []

    #두 집합의 합집합이 전체집합, 번갈아 추가 / Union is the universal set, alternating-ordered
    while index_words < len(words) and index_special < len(special):
        combined.append(words[index_words])
        combined.append(special[index_special])
        index_words += 1
        index_special += 1
    #핵심 단어 / Keywords
    keywords = re.findall(pattern_words, b_line[i])

    #j 추가: 핵심 단어의 개수 / Adding j: The number of keywords
    j = len(keywords)

    #k 추가: 문장에서 단어의 개수 / Adding k: The number of sentences
    k = 0

    print('\n')
    while k < len(combined):
        for x in combined:
            if x in keywords:
                print('___', end = '')
                k += 1
            else:
                print(x, end = '')
                k += 1
            # 단어 추측 / Guessing for the blank
        while j > 0:
            guess = input('\nMake a guess: ')
            print('\n')
            if guess in keywords:
                keywords.remove(guess)
                j -= 1
                if j > 0:
                    print(str(j) + ' left.')
                    for x in combined:
                        if x in keywords:
                            print('___', end = '')
                            k += 1
                        else:
                            print(x, end = '')
                            k += 1
            else:
                print('Try again. ' + str(j) + ' words remain.\n')
                for x in combined:
                    if x in keywords:
                        print('___', end = '')
                    else:
                        print(x, end = '')

        if j == 0:
            k = 0
            while k < len(combined):
                for x in combined:
                    if x in keywords:
                        print('___', end = '')
                        k += 1
                    else:
                        print(x, end = '')
                        k += 1
    i += 1
    print('\nSentence ' + str(i) + ' of ' + str(len(a_line)) + ' complete.\n')

#a와 b 초기화 / Resetting two files, a and b
a.close()
b.close()