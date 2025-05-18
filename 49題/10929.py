while(1):
    a = int(input())
    if(a == 0):
        break   
    if a % 11 == 0:
        print(f'{a} is a multiple of 11.')
    else:
        print(f'{a} is not a multiple of 11.')