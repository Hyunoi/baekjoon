import sys

anum = int(input())
alist = list(map(int, sys.stdin.readline().split()))
bnum = int(input())
blist = list(map(int, sys.stdin.readline().split()))

cnt = []
for i in range(bnum):
    if blist[i] in alist:
        cnt.append(alist.count(blist[i]))
    else:
        cnt.append(0)

for i in range(bnum):
    print(blist[i])
