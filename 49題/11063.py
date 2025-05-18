a = 0
while True:
    try:
        a += 1
        b = int(input())
        c = list(map(int,input().split()))
        ma = [0] * 20003
        t = 0
        for i in range(len(c)):
            for n in range(i, len(c)):
                if c[i] < 1 or c[n] < 1:
                    t = 1
                    break
                if i != n and c[i] >= c[n]:
                    t = 1
                    break
                if ma[c[i] + c[n]] != 0:
                    t = 1
                    break
                ma[c[i] + c[n]] = 1
            if t == 1:
                break
        if t == 1:
            print("Case #%d: It is not a B2-Sequence.\n" % a)
        else:
            print("Case #%d: It is a B2-Sequence.\n" % a)
    except EOFError:
        break