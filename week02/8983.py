import sys

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if animals[mid][0] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

m, n, l = map(int, sys.stdin.readline().split())
guns = list(map(int, sys.stdin.readline().split()))
animals = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if y <= l:
        animals.append((x, y))
animals.sort(key=lambda x: x[1])

answer = 0
for animal in animals:
    left = binary_search(0, m - 1, animal[0] - l + guns[0])
    right = binary_search(0, m - 1, animal[0] + l + guns[-1])
    for i in range(left, right + 1):
        if abs(guns[i] - animal[0]) + animal[1] <= l:
            answer += 1
            break

print(answer)
