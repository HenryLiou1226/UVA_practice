while True:
    try:
        a = int(input())
        print(a * 3 // 2)
    except EOFError:
        break