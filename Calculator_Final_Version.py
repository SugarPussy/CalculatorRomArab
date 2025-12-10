import sys
word = input().split(' ')
operand_3 = int()
operand_4 = ''
word_roman_1 = [(1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(100, 'C'),(90, 'XC'),(50, 'L'),(40, 'XL'),(10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'),(1, 'I')]
word_roman_2 = [(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X')]
if len(word) == 3:
    operand_1 = word[0]
    operand_2 = word[2]
    operator = word[1]
    if operand_1 in 'IIIVIX' and operand_2 in 'IIIVIX':
        for ch, ch1 in word_roman_2:
            if operand_1 == ch1:
                operand_1 = ch
                break
        for elem, elem1 in word_roman_2:
            if operand_2 == elem1:
                operand_2 = elem
                break
        operand_1 = int(operand_1)
        operand_2 = int(operand_2)
        if 1 <= operand_1 < 11 and 1 <= operand_2 < 11:
            if '+' in operator:
                operand_3 = operand_1 + operand_2
            if '*' in operator:
                operand_3 = operand_1 * operand_2
            if '-' in operator:
                operand_3 = operand_1 - operand_2
            if '/' in operator:
                operand_3 = operand_1 / operand_2
        if operand_3 < 1:
            print('Решения нет!')
        for el, el1 in word_roman_1:
            while operand_3 >= el:
                operand_4 += el1
                operand_3 -= el
        print(operand_4)
        sys.exit()
    if operand_1 in '12345678910' and operand_2 in '12345678910':
        operand_1 = int(operand_1)
        operand_2 = int(operand_2)
        if 1 <= operand_1 < 11 and 1 <= operand_2 < 11:
            if '+' in operator:
                operand_3 = operand_1 + operand_2
                print(operand_3)
            if '*' in operator:
                operand_3 = operand_1 * operand_2
                print(operand_3)
            if '-' in operator:
                operand_3 = operand_1 - operand_2
                print(operand_3)
            if '/' in operator:
                operand_3 = operand_1 / operand_2
                print(int(operand_3))
    else:
        print('Решения нет!')
else:
    print('Решения нет!')