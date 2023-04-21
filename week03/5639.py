import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

a=[]

while True:
    try:
        a.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if a[i] > a[start]:
            mid = i
            break
    post(start + 1, mid - 1) #왼쪽 트리
    post(mid, end) #오른쪽 트리
    print(a[start]) #루트 노드

post(0, len(a) - 1)