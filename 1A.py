
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
m = int(input())
print(fib(m))
# упражнение 1

def mn(n, mas):
    i = 2
    while n > 1:
        if n % i == 0:
            mas.append(i)
            n = n // i
            i = 2
        else:
            i += 1
    return mas
s = []
k = int(input())
print(*mn(k, s))
# упражнение 2

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
def Euclid(a, b):
    p = 1
    q = 0
    r = 0
    s = 1
    while a != 0 and b != 0:
        if a >= b:
            a = a - b
            p = p - r
            q = q - s
        else:
            b = b - a
            r = r - p
            s = s - q
    if a != 0:
        x = p
        y = q
    else:
        x = r
        y = s
    return x, y
q = int(input())
ans = []
for _ in range(q):
    a, b = map(int, input().split())
    d = gcd(a, b)
    (x, y) = Euclid(a, b)
    ans.append((x, y, d))
for elem in ans:
    print(*elem)
# упражнение 3


a, b = map(str, input().split())
a = int(a)
for i in range(1, (a + 1) // 2 + 1):
    print(b*i)
for j in range(a//2, 0, -1):
    print(b*j)
# упражнение 4

s = 'U'
mas = []
n, m = map(int, input().split())
for _ in range(n):
    mas.append([0]*m)
print(mas)
i = 0
j = 0
cnt = 1
while cnt < n*m:
    if s == 'U':
        while j < m - 1:
            if mas[i][j + 1] == 0:
                mas[i][j] = cnt
                cnt += 1
                j += 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        i += 1
        s = 'R'
    elif s == 'R':
        while i < n - 1:
            if mas[i + 1][j] == 0:
                mas[i][j] = cnt
                cnt += 1
                i += 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        j -= 1
        s = 'D'
    elif s == 'D':
        while j > 0:
            if mas[i][j - 1] == 0:
                mas[i][j] = cnt
                cnt += 1
                j -= 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        i -= 1
        s = 'L'
    elif s == 'L':
        while i > 0:
            if mas[i - 1][j] == 0:
                mas[i][j] = cnt
                cnt += 1
                i -= 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        j += 1
        s = 'U'
print(mas)
# упражнение 5


n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    t = [int(elem) for elem in input().split()]
    a.append(t[:-1])
    b.append(t[-1])
def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        res = 0
        for i in range(len(matrix)):
            newm = [[elem for j, elem in enumerate(row) if j != i] for row in matrix[1:]]
            res += ((-1)**(i))*matrix[0][i]*det(newm)
        return res
roots = []
delta = det(a)
for i in range(n):
    mat = [[elem if j != i else b[irow] for j, elem in enumerate(row)] for irow, row in enumerate(a)]
    deltai = det(mat)
    print(deltai / delta)
# упражнение 7



