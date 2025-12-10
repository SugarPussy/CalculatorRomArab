import sys
word = input().split(' ')
last_digit = int()
operand_4 = ''
if len(word) == 3:
    operand_1 = word[0]
    operand_2 = word[2]
    operator = word[1]
    if operand_1 in 'IIIVIX' and operand_2 in 'IIIVIX':
        if operand_1 == 'I':
            operand_1 = 1
        if operand_2 == 'I':
            operand_2 = 1
        if operand_1 == 'II':
            operand_1 = 2
        if operand_2 == 'II':
            operand_2 = 2
        if operand_1 == 'III':
            operand_1 = 3
        if operand_2 == 'III':
            operand_2 = 3
        if operand_1 == 'IV':
            operand_1 = 4
        if operand_2 == 'IV':
            operand_2 = 4
        if operand_1 == 'V':
            operand_1 = 5
        if operand_2 == 'V':
            operand_2 = 5
        if operand_1 == 'VI':
            operand_1 = 6
        if operand_2 == 'VI':
            operand_2 = 6
        if operand_1 == 'VII':
            operand_1 = 7
        if operand_2 == 'VII':
            operand_2 = 7
        if operand_1 == 'VIII':
            operand_1 = 8
        if operand_2 == 'VIII':
            operand_2 = 8
        if operand_1 == 'IX':
            operand_1 = 9
        if operand_2 == 'IX':
            operand_2 = 9
        if operand_1 == 'X':
            operand_1 = 10
        if operand_2 == 'X':
            operand_2 = 10
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
                operand_3 = int(operand_3)
        if operand_3 < 1:
            print('Решения нет!')
            sys.exit()
        if operand_3 <= 10:
            if operand_3 == 1:
                print('I')
                sys.exit()
            if operand_3 == 2:
                print('II')
                sys.exit()
            if operand_3 == 3:
                print('III')
                sys.exit()
            if operand_3 == 4:
                print('IV')
                sys.exit()
            if operand_3 == 5:
                print('V')
                sys.exit()
            if operand_3 == 6:
                print('VI')
                sys.exit()
            if operand_3 == 7:
                print('VII')
                sys.exit()
            if operand_3 == 8:
                print('VIII')
                sys.exit()
            if operand_3 == 9:
                print('IX')
                sys.exit()
        if 10 <= operand_3 < 40:
            last_digit = operand_3 % 10
            if last_digit == 0:
                operand_4 += 'X'
            if last_digit == 1:
                operand_4 += 'I'
            if last_digit == 2:
                operand_4 += 'II'
            if last_digit == 3:
                operand_4 += 'III'
            if last_digit == 4:
                operand_4 += 'IV'
            if last_digit == 5:
                operand_4 += 'V'
            if last_digit == 6:
                operand_4 += 'VI'
            if last_digit == 7:
                operand_4 += 'VII'
            if last_digit == 8:
                operand_4 += 'VIII'
            if last_digit == 9:
                operand_4 += 'IX'
            operand_3 = operand_3 // 10
            if operand_3 == 1:
                if last_digit == 0:
                    print(operand_4)
                    sys.exit()
                if last_digit >= 1:
                    print('X' + operand_4)
                    sys.exit()
                if operand_3 == 2:
                    if last_digit == 0:
                        print('X' + operand_4)
                        sys.exit()
                    if last_digit >= 1:
                        print('XX' + operand_4)
                        sys.exit()
                if operand_3 == 3:
                    if last_digit == 0:
                        print('XX' + operand_4)
                        sys.exit()
                    if last_digit >= 1:
                        print('XXX' + operand_4)
                        sys.exit()
        if 40 <= operand_3 < 90:
            last_digit = operand_3 % 10
            if last_digit == 0:
                operand_4 += 'X'
            if last_digit == 1:
                operand_4 += 'I'
            if last_digit == 2:
                operand_4 += 'II'
            if last_digit == 3:
                operand_4 += 'III'
            if last_digit == 4:
                operand_4 += 'IV'
            if last_digit == 5:
                operand_4 += 'V'
            if last_digit == 6:
                operand_4 += 'VI'
            if last_digit == 7:
                operand_4 += 'VII'
            if last_digit == 8:
                operand_4 += 'VIII'
            if last_digit == 9:
                operand_4 += 'IX'
            operand_3 = operand_3 // 10
            if operand_3 == 4:
                if last_digit == 0:
                    print(operand_4 + 'L')
                    sys.exit()
                if last_digit >= 1:
                    print('XL' + operand_4)
                    sys.exit()
            if operand_3 == 5:
                if last_digit == 0:
                    print('L')
                    sys.exit()
                if last_digit >= 1:
                    print('L' + operand_4)
                    sys.exit()
            if operand_3 == 6:
                if last_digit == 0:
                    print('L' + operand_4)
                    sys.exit()
                if last_digit >= 1:
                    print('LX' + operand_4)
                    sys.exit()
            if operand_3 == 7:
                if last_digit == 0:
                    print('LX' + operand_4)
                    sys.exit()
                if last_digit >= 1:
                    print('LXX' + operand_4)
                    sys.exit()
            if operand_3 == 8:
                if last_digit == 0:
                    print('LXX' + operand_4)
                    sys.exit()
                if last_digit >= 1:
                    print('LXXX' + operand_4)
                    sys.exit()
        if 90 <= operand_3 < 101:
            last_digit = operand_3 % 10
            if last_digit == 0:
                operand_4 += 'C'
            if last_digit == 1:
                operand_4 += 'I'
            if last_digit == 2:
                operand_4 += 'II'
            if last_digit == 3:
                operand_4 += 'III'
            if last_digit == 4:
                operand_4 += 'IV'
            if last_digit == 5:
                operand_4 += 'V'
            if last_digit == 6:
                operand_4 += 'VI'
            if last_digit == 7:
                operand_4 += 'VII'
            if last_digit == 8:
                operand_4 += 'VIII'
            if last_digit == 9:
                operand_4 += 'IX'
            operand_3 = operand_3 // 10
            if operand_3 == 9:
                if last_digit == 0:
                    print('X' + operand_4)
                    sys.exit()
                if last_digit >= 1:
                    print('XC' + operand_4)
                    sys.exit()
            if operand_3 == 10:
                if last_digit == 0:
                    print(operand_4)
                    sys.exit()
    if operand_1 in '012345678910' and operand_2 in '012345678910':
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
