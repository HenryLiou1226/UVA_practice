while True:
    try:
        s = str(input())
        ma = -1
        li = []
        ans = 0
        for i in s:
            if i >= '0' and i <= '9':
                li.append(int(i))
                ma = max(ma, int(i))
            elif i >= 'A' and i <= 'Z':
                li.append(ord(i) - ord('A') + 10)
                ma = max(ma, ord(i) - ord('A') + 10)
            elif i >= 'a' and i <= 'z':
                li.append(ord(i) - ord('a') + 36)
                ma = max(ma, ord(i) - ord('a') + 36)
        for i in li:
            ans += i
        t = 0
        for i in range(ma + 1, 63):
            if ans % (i - 1) == 0:
                print(i)
                t = 1
                break
        if t == 0:
            print("such number is impossible!")      
    except EOFError:
        break