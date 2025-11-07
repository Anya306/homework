mas = list(map(int, input().split()))

for i in range(len(mas)):
    k = i + 1
    if k // 2 > 0:
        if mas[i] < mas[k // 2 - 1]:
            print(0)
            exit()
    if k * 2 - 1 < len(mas):
        if mas[i] > mas[k * 2 - 1]:
            print(0)
            exit()
    if k * 2 < len(mas):
        if mas[i] > mas[k * 2 - 1]:
            print(0)
            exit()
print(1)
# задача 1


fr = list(map(int, input().split()))
pl = list(map(int, input().split()))
fo = list(map(int, input().split()))
mas = []
for i in range(len(pl)):
    if pl[i] in fo and (pl[i] not in fr):
        mas.append(pl[i])
mas.sort()
print(*mas)
# задача 2


n = int(input())
d = dict()
for _ in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
mas = sorted(d.items(), key=lambda item: item[1], reverse=True)
for _ in range(len(mas)):
    print(mas[_][0], mas[_][1])
# задача 3


n = int(input())
mas = []
for i in range(n):
    s = list(map(int, input().split()))
    for _ in s:
        mas.append([_, i + 1])
mas.sort()
l = r = 0
mini = len(mas)
mini_in = [0, len(mas)]
d = dict()
for j in range(n):
    d[j + 1] = 0
d[mas[0][1]] = 1
if mas[0][1] == mas[1][1] == mas[2][1] == mas[3][1]:
    print(mas[0][1], '-', mas[0][1])
    exit()

while r < len(mas) - 1:
    while d[1] * d[2] * d[3] * d[4] == 0 and r < len(mas) - 1:
        r += 1
        d[mas[r][1]] += 1
    if mas[r][0] - mas[l][0] <= mini:
        mini = mas[r][0] - mas[l][0]
        mini_in = [mas[l][0], mas[r][0]]
    while d[1] * d[2] * d[3] * d[4] > 0:
        l += 1
        d[mas[l - 1][1]] -= 1
    if mas[r][0] - mas[l - 1][0] <= mini:
        mini = mas[r][0] - mas[l - 1][0]
        mini_in = [mas[l - 1][0], mas[r][0]]
if d[1] * d[2] * d[3] * d[4] > 0:
    while d[1] * d[2] * d[3] * d[4] > 0:
        l += 1
        d[mas[l - 1][1]] = 0
    if mas[r][0] - mas[l - 1][0] <= mini:
        mini = mas[r][0] - mas[l - 1][0]
        mini_in = [mas[l - 1][0], mas[r][0]]
print(mini_in[0], '-', mini_in[1])
# задача 4
