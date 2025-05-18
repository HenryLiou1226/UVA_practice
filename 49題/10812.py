a = int(input())
for i in range(a):
    a,b = map(int, input().split())
    if a < b or (a - b) % 2 == 1:
        print('impossible')
    else:
        ans = (a + b) // 2
        print(f'{max(ans,a - ans)} {min(ans,a - ans)}')