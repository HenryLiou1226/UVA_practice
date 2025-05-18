while True:
    try:
        a = list(map(float, input().split()))
        t = [0,0,0,0]
        ans = [0,0]
        for i in range(4):
            for j in range(i + 1, 4):
                if a[i * 2] == a[j * 2] and a[i * 2 + 1] == a[j * 2 + 1]:
                    ans[0] = -a[i * 2]
                    ans[1] = -a[i * 2 + 1]
                    t[i] = 1
                    t[j] = 1
                    break
        for i in range(4): 
            if t[i] == 0:
                ans[0] += a[i * 2]
                ans[1] += a[i * 2+ 1]
        print(f'{ans[0]:.3f} {ans[1]:.3f}')
                    
        
    except EOFError:
        break