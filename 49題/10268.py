while True:
    try:
        a = int(input())
        ar = list(map(int, input().split()))
        ar = ar[::-1]
        ans = 0
        temp = 1
        cur = 0
        for i in range(1,len(ar)):
            cur += 1
            ans += ar[i] * temp * cur
            temp *= a
        print(ans)
    except EOFError:
        break