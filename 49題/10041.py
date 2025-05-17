a = int(input())
for i in range(a):
    n = list(map(int,input().split()))
    n = n[1:]
    n.sort()
    mid = n[len(n) // 2] 
    ans = 0
    for i in n:
        ans += abs(i - mid)
    print(ans)