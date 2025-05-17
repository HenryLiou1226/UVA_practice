a = [0] * 50
a[0] = 1
a[1] = 2
for i in range(2,50):
    a[i] = a[i-1] + a[i-2]
l = int(input())
for i in range(l):
    n = int(input())
    ans1 = n
    ans = ''
    st = 0
    for i in range(49, -1, -1):
        if n >= a[i]:
            n -= a[i]
            ans += '1'
            st = 1
        elif n < a[i] and st == 1:
            ans += '0'
    print(f'{ans1} = {ans} (fib)')