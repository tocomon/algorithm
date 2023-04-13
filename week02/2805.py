import sys

def get_cut_length(height, tree):
    cut_length = 0
    for t in tree:
        if t > height:
            cut_length += t - height
    return cut_length

N, M = list(map(int, sys.stdin.readline().split()))
tree = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(tree)
max_height = 0
while left <= right:
    mid = (left + right) // 2
    cut_length = get_cut_length(mid, tree)
    if cut_length >= M:
        max_height = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_height)


# 시간 초과
# import sys
# N, M = list(map(int, sys.stdin.readline().split()))
# tree = list(map(int, sys.stdin.readline().split()))

# toptree=max(tree)

# maxresult=0
# maxheight=0
# for i in range(toptree):
#     result=0
#     for tr in tree:
#         if tr>toptree-i-1:
#             result+=tr-toptree+i+1
#     maxresult=max(result,maxresult)
#     if maxresult>M:
#         maxheight=toptree-i
#         break

# print(maxheight)