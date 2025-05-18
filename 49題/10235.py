a = [0] * 1000003
for i in range(2,int(len(a) ** 0.5) + 1):
    if a[i] == 0:
        for j in range(i * i, len(a), i):
            a[j] = 1
while True:
    try:
        b = str(input())
        c = int(b)
        d = int(b[::-1])
        if a[c] == 1:
            print(c, "is not prime.")
        elif a[c] == 0 and a[d] == 0 and c != d:
            print(c, "is emirp.")
        else:
            print(c, "is prime.")
    except EOFError:
        break