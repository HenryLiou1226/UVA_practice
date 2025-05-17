while True:
    try:
        a = int(input())
        arr = [0] * a
        for i in range(a):
            arr[i] = int(input())
        arr.sort()
        mid = 0
        if a % 2 == 0:
            mid = arr[a // 2 - 1]
            ans2 = arr.count(mid) + arr.count(arr[a // 2]) if mid != arr[a // 2] else arr.count(mid)
        else:
            mid = arr[a // 2]
            ans2 = arr.count(mid)
        ans3 = arr[a // 2] - mid + 1
        print(f'{mid} {ans2} {ans3}')
    except EOFError:
        break
    