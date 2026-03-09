n = int(input())
st = []
for _ in range(n):
    a, b = map(int, input().split())
    st.append((a, b))
mas = []
for i in range(n):
    for j in range(i + 1, n):
        x = st[i][0] - st[j][0]
        y = st[i][1] - st[j][1]
        dist = (x ** 2 + y ** 2) ** 0.5
        mas.append((dist, i, j))
mas.sort()
p = [0] * n
for j in range(n):
    p[j] = j
for i in range(len(mas)):
    a = mas[i][1]
    while p[a] != a:
        a = p[a]
    b = mas[i][2]
    while p[b] != b:
        b = p[b]
    if a != b:
        p[a] = b
    if mas[i][0] * 1000 % 10 >= 5:
        print((mas[i][0] * 1000 + 1) // 1 / 1000)
    else:
        print((mas[i][0] * 1000) // 1 / 1000)
    break
#задача 1


c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    mas = []
    for i in range(m):
        x, y, t = map(int, input().split())
        mas.append((x, y, t))
    d = [10**9] * n
    d[0] = 0
    for i in range(n - 1):
        for j in range(m):
            x, y, t = mas[j]
            if d[x] + t < d[y]:
                d[y] = d[x] + t
    flag = False
    for j in range(m):
        x, y, t = mas[j]
        if d[x] + t < d[y]:
            flag = True
            break

    if flag:
        print("возможно")
    else:
        print("не возможно")
#задача 2

