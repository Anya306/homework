n = int(input())
a = [0] * n
b = [0] * n
for z in range(n):
    a[z], b[z] = map(int, input().split())
visited = [False] * n  # использовано visited вместо used
d = [float('inf')] * n
d[0] = 0
mini = 0
for _ in range(n):
    v = -1
    m = float('inf')
    for i in range(n):
        if not visited[i] and d[i] < m:
            m = d[i]
            v = i
    visited[v] = True
    mini += m ** 0.5
    for i in range(n):
        if not visited[i]:
            if (a[v] - a[i]) ** 2 + (b[v] - b[i]) ** 2 < d[i]:
                d[i] = (a[v] - a[i]) ** 2 + (b[v] - b[i]) ** 2

print(mini)
# задача 1


import queue

n = int(input())
mas1 = input().split()
m, l = map(int, input().split())
mas2 = []
for _ in range(m):
    mas2.append(input().split())
res = []
for w in mas1:
    flag = False
    if len(w) == 1:
        for i in range(m):
            for j in range(l):
                if mas2[i][j] == w[0]:
                    flag = True
                    break
            if flag:
                break
    else:
        for i in range(m):
            for j in range(l):
                if mas2[i][j] == w[0]:
                    q = queue.Queue()
                    q.put((i, j, 1, [(i, j)]))
                    while not q.empty():
                        x, y, ind, visited = q.get()
                        if ind == len(w):
                            flag = True
                            break
                        for a in [-1, 0, 1]:
                            for b in [-1, 0, 1]:
                                if a == 0 and b == 0:
                                    continue
                                if 0 <= x + a < m and 0 <= y + b < l:
                                    if (x + a, y + b) not in visited and mas2[x + a][y + b] == w[ind]:
                                        q.put((x + a, y + b, ind + 1, visited + [(x + a, y + b)]))
                        if flag:
                            break
                    if flag:
                        break
            if flag:
                break
    if flag:
        res.append(w)
res.sort()
for i in range(len(res)):
    print(res[i], end='')


# задача 2


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True


def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w, i))
    sorted_edges = sorted(edges, key=lambda x: x[2])
    dsu = DSU(n)
    mst_weight = 0
    flag = [False] * m
    tree = [[] for _ in range(n)]
    for u, v, w, k in sorted_edges:
        if dsu.union(u, v):
            mst_weight += w
            flag[k] = True
            tree[u].append((v, w))
            tree[v].append((u, w))

    def max_on_path(a, b):
        q = queue.Queue()
        q.put((a, -1, 0))
        while not q.empty():
            c, p, ma = q.get()
            if c == b:
                return ma
            for o, w in tree[cur]:
                if o != p:
                    q.put((nxt, cur, max(ma, w)))
        return 0

    res = [0] * m
    for u, v, w, k in edges:
        if flag[k]:
            res[k] = we
        else:
            maxi = max_on_path(u, v)
            res[k] = we - maxi + w
    for x in ans:
        print(x)


if __name__ == "__main__":
    main()

# задача 4
