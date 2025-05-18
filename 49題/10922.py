while(1):
    a = int(input())
    c = 1
    if(a == 0):
        break
    print(a,end='')
    b = 0
    while(a > 0):
        b = b + a % 10
        a = a//10
    if(b % 9 != 0):
        print(" is not a multiple of 9.")
    else:
        while(b > 9):
            d = 0
            while(b > 0):
                d = d + b%10
                b = b//10
            c = c+1
            b = d
        print(" is a multiple of 9 and has 9-degree {}.".format(c))