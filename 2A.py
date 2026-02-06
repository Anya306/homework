import queue
n = int(input())
graf = dict()
visited = []
s = set()
d = input()
while d != '':
    a, b = map(int, d.split())
    if a not in graf:
        graf[a] = [b]
    else:
        graf[a].append(b)
    if b not in graf:
        graf[b] = [a]
    else:
        graf[b].append(a)
    d = input()
q = queue.Queue()
for i in graf[0]:
    q.put(i)
while not q.empty():
    x = q.get()
    s.add(x)
    if x in visited:
        continue
    else:
        visited.append(x)
    for j in graf[x]:
        q.put(j)
if n == len(s):
    print("True")
else:
    print("False")
# задача 1


n = int(input())
graf = dict()
for z in range(n):
    graf[z] = []
visited = []
d = input()
while d != '':
    a, b = map(int, d.split())
    graf[a].append(b)
    d = input()
a, b = map(int, input().split())
flag = False
q = queue.Queue()
for i in graf[a]:
    q.put(i)
while not q.empty():
    x = q.get()
    if x == b:
        flag = True
    if x in visited:
        continue
    else:
        visited.append(x)
    for j in graf[x]:
        q.put(j)
if flag:
    print("True")
else:
    print('False')
# задача 2



n = int(input())
graf = dict()
for z in range(n):
    graf[z] = []
visited = []
d = input()
while d != '':
    a, b = map(int, d.split())
    graf[a].append(b)
    d = input()
flag = False
q = queue.Queue()
for i in graf[0]:
    q.put(i)
while not q.empty():
    x = q.get()
    if x in visited:
        flag = True
        continue
    else:
        visited.append(x)
    for j in graf[x]:
        q.put(j)
if flag:
    print("True")
else:
    print('False')
# задача 4



graf = dict()
visited = []
d = input()
while d != '':
    a, b = map(str, d.split())
    if a not in graf:
        graf[a] = b
    else:
        graf[a].append(b)
    d = input()
mas = []
q = queue.Queue()
k = list(graf.keys())
val = list(graf.values())
for w in k:
    if w not in val:
        mas.append(w)
        break
for i in graf[w]:
    q.put(i)
while not q.empty():
    a = q.get()
    b = q.get()
    c = q.get()
    x = a + b + c
    mas.append(x)
    if x in visited:
        continue
    else:
        visited.append(x)
    if x not in graf:
        break
    else:
        for j in graf[x]:
            q.put(j)
print(*mas)
# задача 3



graf = dict()
visited = []
d = input()
r = d[0]
while d != '':
    a = d[0]
    b = d[-1]
    if a not in graf:
        graf[a] = [b]
    else:
        graf[a].append(b)
    d = input()
flag = False
q = queue.Queue()
for i in graf[r]:
    q.put(i)
while not q.empty():
    x = q.get()
    if x in visited:
        flag = True
        continue
    else:
        visited.append(x)
    for j in graf[x]:
        q.put(j)
if flag:
    print("True")
else:
    print('False')
# задача 6 



n = int(input())
graf = dict()
for w in range(n):
    graf[w] = []
visited = [0] * n
d = input()
r = d[0]
ves = 0
while d != '':
    a, b, c = map(int, d.split())
    graf[a].append([b, c, a])
    d = input()
a, b = map(int, input().split())
q = queue.Queue()
for i in graf[a]:
    q.put(i)
while not q.empty():
    x = q.get()
    if visited[x[0]] == 0:
        visited[x[0]] = x[1] + visited[x[2]]
    else:
        visited[x[0]] = min(x[1] + visited[x[2]], visited[x[0]])
    for j in graf[x[0]]:
        q.put(j)
print(visited[b])
# задача 5