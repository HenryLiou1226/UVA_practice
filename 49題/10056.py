a = int(input())
for i in range(a):
    a,b,c = input().split()
    a = int(a)
    b = float(b)
    c = int(c)
    fi = ((1 - b) ** (c - 1))* b
    ans = fi / (1 - (1 -b) ** (a))
    print('%.4f' % ans) 