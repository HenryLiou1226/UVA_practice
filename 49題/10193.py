def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
a = int(input())
for i in range(a):
    a = input()
    b = input()
    a = int(a,2)
    b = int(b,2)
    ans = gcd(a,b)
    if ans != 1:
        print(f'Pair #{i + 1}: All you need is love!')
    else:
        print(f'Pair #{i + 1}: Love is not all you need!')