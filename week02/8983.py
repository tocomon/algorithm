import sys

def count_animals(x_pos, y_pos, hunters, L):
    count = 0
    for x, y in zip(x_pos, y_pos):
        left = 0
        right = len(hunters) - 1
        while left <= right:
            mid = (left + right) // 2
            if abs(hunters[mid] - x) + y <= L:
                count += 1
                break
            elif hunters[mid] > x:
                if mid == left:
                    break
                right = mid - 1
            else:
                if mid == right:
                    break
                left = mid + 1
    return count

M, N, L = map(int, input().split())
hunters = sorted(map(int, input().split()))
x_pos = []
y_pos = []
for i in range(N):
    x, y = map(int, input().split())
    if y > L:
        continue
    x_pos.append(x)
    y_pos.append(y)
print(count_animals(x_pos, y_pos, hunters, L))
