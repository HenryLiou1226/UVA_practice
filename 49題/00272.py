cnt = 0
while True:
    try:
        a = str(input())
        for i in a:
            if i == '"' and cnt == 0:
                cnt = 1
                print('``', end='')
            elif i == '"' and cnt == 1:
                cnt = 0
                print("''", end='')
            else:
                print(i, end='')
        print()
    except EOFError:
        break