import sys
T = int(sys.stdin.readline())
for i in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    
    new_s = ""
    for char in S:
        new_s += char * R
    print(new_s)
