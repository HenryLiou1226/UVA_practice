cnt = 0
while True:
    try:
        cnt += 1
        if cnt != 1:
            print()
        a,b = map(int,input().split())
        if a == 0 and b == 0:
            break
        arr = [['.' for _ in range(b + 2)] for _ in range(a + 2)]
        for i in range(a):
            s = str(input())
            for j in range(b):
                arr[i + 1][j + 1] = s[j]
        for i in range(1,a + 1):
            for j in range(1,b + 1):
                if arr[i][j] == '.':
                    arr[i][j] = 0
                    for k in range(-1,2):
                        for l in range(-1,2):
                            if arr[i + k][j + l] == '*':
                                arr[i][j] += 1
        print(f'Field #{cnt}:')
        for i in range(1,a + 1):
            for j in range(1,b + 1):
                print(arr[i][j], end='')
            print()
    except EOFError:
        break