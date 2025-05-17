while True:
    try:
        s,d = map(int,input().split())
        n = int((-1+((1-4*s+4*(s**2)+8*d)) ** 0.5)/2)
        if ((n + s) * (n - s + 1) ) // 2 < d:
            n += 1
        print(n)
    except EOFError:
        break