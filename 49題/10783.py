a = int(input())
for i in range(a):
    s = int(input())
    e = int(input())
    if s % 2 == 0:
        s += 1
    if e % 2 == 0:
        e -= 1
    ans = (e + s) * ((e - s) // 2 + 1) // 2
    print(f'Case {i + 1}: {ans}')