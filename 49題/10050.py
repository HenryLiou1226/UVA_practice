a = int(input())
for i in range(a):
    n = int(input())
    arr = [0] * n
    t = int(input())
    for j in range(t):
        d = int(input())
        for k in range(d - 1,n,d):
            arr[k] = 1
    ans = 0
    for l in range(n):
        if ((l % 7) % 6 == 0 or (l % 7) % 5 == 0) and l % 7 != 0:
            continue
        elif arr[l] > 0:
            ans += 1
    print(ans)