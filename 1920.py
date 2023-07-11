import sys

# 1
nnum = int(input())
nlist = set(map(int, sys.stdin.readline().split()))

mnum = int(input())
mlist = list(map(int, sys.stdin.readline().split()))
 
for i in mlist:
    if i in nlist:
        print(1)
    else:
        print(0)