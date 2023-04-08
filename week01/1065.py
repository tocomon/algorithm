import sys  
a = int(sys.stdin.readline())

count=0
if a < 100:
    print(a)
elif a>=100:
    count+=99
    for i in range(100,a):
        diff1 = int(str(i)[0])-int(str(i)[1])
        diff2 = int(str(i)[1])-int(str(i)[2])
        if diff1 == diff2:
            count += 1
    print(count)