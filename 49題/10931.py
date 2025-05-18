while(1):
    a = int(input())
    if(a == 0):
        break
    a = bin(a)[2:]
    print(f'The parity of {a} is {a.count("1")} (mod 2).')