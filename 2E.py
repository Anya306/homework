
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
        dist = (x**2 + y**2) ** 0.5
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