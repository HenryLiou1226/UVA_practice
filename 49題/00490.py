a = []
to = 0
while True:
    try:
        s = str(input())
        a.append(s)
        to = max(to, len(s))
    except EOFError:
        break
for i in range(to):
    for j in range(len(a) - 1, -1, -1):
        if i < len(a[j]):
            print(a[j][i], end='')
        else:
            print(' ', end='')
    print()