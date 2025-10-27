from collections import deque

deque0 = deque(input())
print(deque0)
deque1 = deque()
res = []
zn = ['-', '+', '*', '/']

while len(deque0) > 0:
    if deque0[0] == '(':
        deque1.appendleft(deque0[0])
        deque0.popleft()
    elif deque0[0] == ')':
        deque0.popleft()
        while deque1[0] != '(':
            res.append(deque1[0])
            deque1.popleft()
        deque1.popleft()
    elif deque0[0] in zn:
        if len(deque1) > 0:
            if deque1[0] == '*':
                while len(deque1) > 0 and deque1[0] != '(':
                    res.append(deque1[0])
                    deque1.popleft()
                deque1.appendleft(deque0[0])
                deque0.popleft()
            elif deque1[0] == '+' and (deque0[0] == '+' or deque0[0] == '-'):
                while len(deque1) > 0 and deque1[0] != '(':
                    res.append(deque1[0])
                    deque1.popleft()
                deque1.appendleft(deque0[0])
                deque0.popleft()
            else:
                deque1.appendleft(deque0[0])
                deque0.popleft()
        else:
            deque1.appendleft(deque0[0])
            deque0.popleft()
    else:
        res.append(deque0[0])
        deque0.popleft()
    print(deque1, deque0)
while len(deque1) > 0:
    res.append(deque1[0])
    deque1.popleft()
print(*res)