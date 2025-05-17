a = int(input())
for i in range(a):
    n = int(input())
    ans1 = bin(n)[2:].count('1')
    n = int(str(n),16)
    ans2 = bin(n)[2:].count('1')
    print(f'{ans1} {ans2}')