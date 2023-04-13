n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])

start, end = 1, houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    count = 1
    prev = houses[0]
    
    for i in range(1, n):
        if houses[i] - prev >= mid:
            count += 1
            prev = houses[i]
    
    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)



# import sys
# N, C = list(map(int, sys.stdin.readline().split()))
# a=[]
# for _ in range(N):
#     a.append(int(sys.stdin.readline().strip()))

# a.sort()
# b=[]
# for i in range(len(a)-1):
#     b.append(a[i+1]-a[i])

# print(b)