import sys
input = sys.stdin.readline

def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def closest_pair(points):
    n = len(points)
    if n <= 3:
        return min(dist(points[i], points[j]) for i in range(n) for j in range(i+1, n))
    mid = n//2
    left = points[:mid]
    right = points[mid:]
    d = min(closest_pair(left), closest_pair(right))
    strip = [p for p in points if (p[0]-points[mid][0])**2 < d]
    strip.sort(key=lambda x:x[1])
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1]-strip[i][1])**2 >= d:
                break
            d = min(d, dist(strip[i], strip[j]))
    return d

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort()
print(closest_pair(points))


# 시간초과
# import sys

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

# result = sys.maxsize
# for i in a:
#     a_max = sys.maxsize
#     a.remove(i)
#     for j in a:
#         a_max = min(a_max, (i[0]-j[0])**2+(i[1]-j[1])**2)
#     result = min(a_max, result)

# print(result)