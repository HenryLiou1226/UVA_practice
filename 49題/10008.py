a = int(input())
dic = {}
for i in range(a):
    s = str(input())
    s = s.upper()
    for j in s:
        if j.isalpha():
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
ans = sorted(dic.items(),key = lambda x:(-x[1],x[0]))
for i in ans:
    print(f'{i[0]} {i[1]}')