a = int(input())
dic = {}
for i in range(a):
    s = list(map(str, input().split()))
    if s[0] not in dic:
        dic[s[0]] = 1
    else:
        dic[s[0]] += 1
ans = sorted(dic.items())
for i in ans:
    print(f'{i[0]} {i[1]}')
    