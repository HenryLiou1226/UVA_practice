while True:
    try:
        a = [0] * 26
        b = [0] * 26
        s1 = str(input())
        s2 = str(input())
        for i in s1:
            if i.isalpha():
                a[ord(i) - ord('a')] += 1
        for i in s2:
            if i.isalpha():
                b[ord(i) - ord('a')] += 1
        ans = ''
        for i in range(26):
            if a[i] != 0 and b[i] != 0:
                ans += chr(i + ord('a')) * min(a[i], b[i])
        print(ans)
    except EOFError:
        break