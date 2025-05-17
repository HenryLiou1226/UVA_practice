while True:
    try:
        a,b = map(str,input().split())
        if a == '0' and b == '0':
            break
        a = a[::-1]
        b = b[::-1]
        ca = 0
        cur = 0
        ans = 0
        for i in range(max(len(a), len(b))):
            if i < len(a):
                cur += int(a[i])
            if i < len(b):
                cur += int(b[i])
            cur += ca
            if cur >= 10:
                ca = 1
                ans += 1
            else:
                ca = 0
            cur = 0
        if ans == 0:
            print("No carry operation.")
        elif ans == 1:
            print(f"{ans} carry operation.")
        else:
            print(f"{ans} carry operations.")
    except EOFError:
        break
