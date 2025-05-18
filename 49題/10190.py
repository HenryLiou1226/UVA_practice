while(1):
    try:
        n,m = map(int,input().split())
        if(m == 0):
            print('Boring!')
            continue
        c = []
        while(n > 1):
            d = [n]
            c = c + d
            if(n/m == n//m):
                n = n//m
            else:
                break
        if(n == 1):
            c = c + [1]
            for i in c:
                print(i,end = ' ')
            print()
        else:
            print('Boring!')
    except EOFError:
        break