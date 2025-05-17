a,b = map(int,input().split())
c = [[0 for i in range(a+100)]for i in range(b+100)]
#n s e w
while True:
    try:
        d = list(input().split())
        sx = int(d[0])
        sy = int(d[1])
        w = str(d[2])
        t = 0
        way = ['E','S','W','N']
        for i in range(4):
            if w == way[i]:
                w = int(i)
        s = str(input())
        for i in s:
            if(i == 'L'):
                if(w == 0):
                    w = 3
                else:
                    w -= 1
            elif(i == 'R'):
                w = (w+1)%4
            elif(i == 'F'):
                if(w == 0):
                    if(sx == a and c[sx][sy] == 0):
                        print(f"{sx} {sy} {way[w]} LOST")
                        c[sx][sy] = 1
                        t = 1
                        break
                    elif(sx == a and c[sx][sy] == 1):
                        continue
                    elif(sx < a):
                        sx += 1
                elif(w == 1):
                    if(sy == 0 and c[sx][sy] == 0):
                        print(f"{sx} {sy} {way[w]} LOST")
                        c[sx][sy] = 1
                        t = 1
                        break
                    elif(sy == 0 and c[sx][sy] == 1):
                        continue
                    else:
                        sy -= 1
                elif(w == 2):
                    if(sx == 0 and c[sx][sy] == 0):
                        print(f"{sx} {sy} {way[w]} LOST")
                        c[sx][sy] = 1
                        t = 1
                        break
                    elif(sx == 0 and c[sx][sy] == 1):
                        continue
                    else:
                        sx -= 1
                elif(w == 3):
                    if(sy == b and c[sx][sy] == 0):
                        c[sx][sy] = 1
                        print(f"{sx} {sy} {way[w]} LOST")
                        t = 1
                        break
                    elif(sy == b and c[sx][sy] == 1):
                        continue
                    elif(sy < b):
                        sy += 1
        if(t == 0):
            print(f"{sx} {sy} {way[w]}")
    except EOFError:
        break