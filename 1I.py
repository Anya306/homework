'''
def build_tree_maxi(a):
    tree = {}
    for i in range(n):
        tree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    return tree

def max_tree(tree, l, r):
    maxi = 0
    l += n
    r += n
    while l < r:
        if (l & 1) > 0:
            maxi = max(maxi, tree[l])
            l += 1
        if (r & 1) > 0:
            r -= 1
            maxi = max(maxi, tree[r])
        l = l // 2
        r = r // 2
    return maxi

global n
n = int(input())
mas = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(max_tree(build_tree_maxi(mas), l, r))
# задача 1
'''

'''
def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)


def build_tree_gcd(a):
    tree = {}
    for i in range(n):
        tree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
    return tree


def gcd_tree(tree, l, r):
    m = 0
    l += n
    r += n
    while l < r:
        if (l & 1) > 0:
            m = gcd(m, tree[l])
            l += 1
        if (r & 1) > 0:
            m = gcd(m, tree[r])
            r -= 1
        l = l // 2
        r = r // 2
    if m == 0:
        m = tree[l]
    return m


global n
n = int(input())
mas = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(gcd_tree(build_tree_gcd(mas), l, r))
# задача 2
'''


def build_tree_zero(a):
    tree = {}
    for i in range(n):
        if a[i] == 0:
            tree[n + i] = str(i)
        else:
            tree[n + i] = ''
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2 * i] + ' ' + tree[2 * i + 1]
    return tree


def zero_tree(tree, l, r, k):
    s = ''
    l += n
    r += n
    while l <= r:
        if (l & 1) > 0:
            s += tree[l]
            l += 1
        if (r & 1) > 0:
            s += tree[r]
            r -= 1
        l = l // 2
        r = r // 2
    mas = s.split()
    if len(mas) >= k:
        return mas[k - 1]
    else:
        return 0


global n
n = int(input())
mas = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    l, r, k = map(int, input().split())
    print(zero_tree(build_tree_zero(mas), l, r, k))


