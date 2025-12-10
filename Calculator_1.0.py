word = input().split(' ')
operand_1 = int(word[0])
operand_2 = int(word[2])
operator = word[1]
if len(word) == 3:
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
        print('Не меньше 1 и не больше 10!')
if len(word) > 3:
    print('Решения нет!')
