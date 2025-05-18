a = int(input())
b = input()
for _ in range(a):
    if _ != 0:
        print()
    ans = {}
    count = 0
    while True:
        try:
            c = str(input())
            if c == '':
                break
            count += 1
            if c not in ans:
                ans[c] = 1
            else:
                ans[c] += 1
        except EOFError:
            break
    ans = sorted(ans.items())
    for n in ans:
        print(f'{n[0]} {n[1] * 100 / count:.4f}')