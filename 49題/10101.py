def solve(a):
    if a >= 10000000:
        solve(a // 10000000)
        print(" kuti", end="")
        a %= 10000000
    if a >= 100000: 
        solve(a // 100000)
        print(" lakh", end="")
        a %= 100000
    if a >= 1000:
        solve(a // 1000)
        print(" hajar", end="")
        a %= 1000
    if a >= 100:
        solve(a // 100)
        print(" shata", end="")
        a %= 100
    if a:
        print(f" {a}", end="")
cnt = 0
while True:
    try:
        cnt += 1
        a = int(input())
        print(f"{cnt}.", end="")
        if a == 0:
            print(" 0")
        else:
            solve(a)
        print()
    except EOFError:
        break