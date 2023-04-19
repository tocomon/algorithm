from collections import deque
a = int(input())

result=deque([])

for i in range(a):
    result.append(i+1)

while len(result)!=1:
    result.popleft()
    result.append(result.popleft())

print(result[0])