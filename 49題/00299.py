a = int(input())
for i in range(a):
    ans = 0
    l = int(input())
    ar = list(map(int,input().split()))
    for k in range(l - 1):
        for j in range(len(ar) - k - 1):
            if ar[j] > ar[j + 1]:
                ans += 1
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
    print(f"Optimal train swapping takes {ans} swaps.")
