import sys


def dijkstra(graph, start, n):
    unvisited_vertices = list(range(n))
    shortest_path = {}
    previous_vertex = {}

    max_value = sys.maxsize
    for vertex in unvisited_vertices:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0

    while unvisited_vertices:
        # ищем вершину с минимальной оценкой
        current_min_vertex = None
        for vertex in unvisited_vertices:
            if current_min_vertex is None:
                current_min_vertex = vertex
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex

        if shortest_path[current_min_vertex] == max_value:
            break

        # получаем соседей текущей вершины
        if current_min_vertex in graph:
            neighbors = graph[current_min_vertex]
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_vertex] + neighbors[neighbor]
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_vertex[neighbor] = current_min_vertex

        unvisited_vertices.remove(current_min_vertex)

    return previous_vertex, shortest_path


def count_path_vertices(previous_vertex, start_vertex, target_vertex):
    path = []
    vertex = target_vertex

    while vertex != start_vertex:
        path.append(vertex)
        vertex = previous_vertex[vertex]
    path.append(start_vertex)

    return len(path)


graf = {}
n, m, s, f = map(int, input().split())
for _ in range(m):
    v1, v2, weight = map(int, input().split())

    if v1 not in graf:
        graf[v1] = {}
    if v2 not in graf:
        graf[v2] = {}

    graf[v1][v2] = weight
    graf[v2][v1] = weight

previous_vertex, shortest_path = dijkstra(graf, s, n)
print(count_path_vertices(previous_vertex, s, f))


# задача 1


def is_cyclic(graph_array: list[list[int]]) -> bool:
    used = [False] * len(graph_array)
    res = False

    def dfs(v, p=-1):
        nonlocal res  # Исправлено: нужно объявить как nonlocal
        used[v] = True
        for u in graph_array[v]:
            if not used[u]:
                dfs(u, v)  # Исправлено: dfs(u, v) вместо dfs[u, v]
                if res:
                    return
            elif u != p:
                res = True
                return

    for i in range(len(graph_array)):
        if not used[i]:
            dfs(i)  # Исправлено: dfs(i) вместо dfs[i]
            if res:
                break

    return res


V, E = map(int, input().split())

d = input().strip()
d = d.replace('{', '').replace('}', '').split('}, {')

graf = []
for i in range(V):
    if i < len(d) and d[i].strip():
        neighbors = list(map(int, d[i].split(',')))
        graf.append(neighbors)
    else:
        graf.append([])

if is_cyclic(graf):
    print('YES')
else:
    print('NO')


# задача 2


def build_conflict_graph(n, start_times, end_times):
    graph = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            if not (end_times[i] <= start_times[j] or end_times[j] <= start_times[i]):
                graph[i].append(j)
                graph[j].append(i)

    return graph


def max_meetings(n, st, endt):
    meetings = []
    for i in range(n):
        meetings.append((st[i], endt[i]))

    meetings.sort(key=lambda x: x[1])

    count = 0
    lt = -1

    for s, e in meetings:
        if s > lt:
            count += 1
            lt = e

    return count


n = int(input())
st = list(map(int, input().split()))
endt = list(map(int, input().split()))

conflict_graph = build_conflict_graph(n, st, endt)
result = max_meetings(n, st, endt)
print(result)
# задача 3


n = int(input())
m = int(input())

g = {}
for i in range(n):
    g[i] = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

visited = [False] * n


def dfs(start, visited, g):
    visited[start] = True
    for u in g[start]:
        if not visited[u]:
            dfs(u, visited, g)


count = 0
for i in range(n):
    if not visited[i]:
        dfs(i, visited, g)
        count += 1

print(count)
# задача 6


n, m = map(int, input().split())
V = {}
for i in range(n):
    V[i] = []
for _ in range(m):
    v1, v2 = map(int, input().split())
    V[v1].append(v2)
    V[v2].append(v1)
start = 0
D = [None] * n
D[start] = 0
Q = [start]
Qstart = 0
while Qstart < len(Q):
    u = Q[Qstart]
    Qstart += 1
    for v in V[u]:
        if D[v] is None:
            D[v] = D[u] + 1
            Q.append(v)

for i in range(n):
    print(D[i])
# задача 5
