# import sys
# while True:
#     input_list = list(map(int, sys.stdin.readline().split()))
#     if input_list[0] == 0:
#         break
#     input_list.append(0)
#     ret = 0
#     stack = [[0, 0]]
#     for i in range(1, input_list[0] + 2):
#         while stack[-1][1] > input_list[i]:
#             tmp_list = stack.pop()
#             tmp_area = 0
#             while stack[-1][1] == tmp_list[1]:
#                 stack.pop()
#             tmp_area = max((i - 1 - stack[-1][0]) * tmp_list[1], (i - tmp_list[0]) * tmp_list[1])
#             if tmp_area > ret:
#                 ret = tmp_area
#         stack.append([i, input_list[i]])
#     print(ret)

while True:
    n, *heights = map(int, input().split())
    if n == 0:
        break

    stack = []  # 스택 초기화
    max_area = 0  # 최대 넓이 초기화

    for i, h in enumerate(heights):
        left = i  # 왼쪽 끝 인덱스 초기화
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()  # 스택에서 pop하여 인덱스와 높이를 얻음
            area = height * (i - idx)  # pop한 직사각형의 넓이 계산
            left = idx  # pop한 직사각형의 왼쪽 인덱스를 왼쪽 끝으로 설정
            max_area = max(max_area, area)  # 최대 넓이 갱신
        stack.append((left, h))  # 현재 직사각형 스택에 push

    # 스택이 비어있지 않다면, 스택의 top에 있는 직사각형을 기준으로 오른쪽 끝이 n인 직사각형의 넓이 계산하여 최대값 갱신
    while stack:
        idx, height = stack.pop()
        area = height * (n - idx)
        max_area = max(max_area, area)

    print(max_area)
