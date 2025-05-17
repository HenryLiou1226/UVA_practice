t = 0
while True:
    try:
        if t == 1:
            print()
        a = {}
        s = str(input())
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        ans = sorted(a.items(), key=lambda x: (x[1], -ord(x[0])))
        for i in ans:
            print(f'{ord(i[0])} {i[1]}')
        t = 1
    except EOFError:
        break