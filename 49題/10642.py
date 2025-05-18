a = int(input())
for i in range(a):
    a,b,c,d = map(int, input().split())
    st = ((1 + (a + b)) * (a + b)) // 2 + (a)
    ed = ((1 + (c + d)) * (c + d)) // 2 + (c)
    ans = ed - st
    print(f'Case {i + 1}: {ans}')