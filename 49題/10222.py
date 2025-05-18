a = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
while True:
    try:
        n = str(input())
        for i in n:
            if i == ' ':
                print(' ', end='')
            else:
                print(a[a.index(i)-2], end='')
        print()
    except EOFError:
        break