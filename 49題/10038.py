while True:
    try:
        ar = list(map(int, input().split()))
        n = ar[0]
        ar = ar[1:]
        sa = [0] * n
        t = 0
        for i in range(n - 1):
            if abs(ar[i] - ar[i + 1]) > n - 1:
                t = 1
                break
            if sa[abs(ar[i] - ar[i + 1])] == 0:
                sa[abs(ar[i] - ar[i + 1])] = 1
            else:
                t = 1
                break
        if t == 1:
            print("Not jolly")
        else:
            print("Jolly")
    except EOFError:
        break
