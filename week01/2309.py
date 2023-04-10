import sys  
a = [int(sys.stdin.readline()) for i in range(9)]

total = sum(a)

dwarf1=0
dwarf2=0

for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if 100 == total - a[i] - a[j]:
                dwarf1=a[i]
                dwarf2=a[j]
                break

a.remove(dwarf1)
a.remove(dwarf2)

a.sort()

for i in a:
    print(i)