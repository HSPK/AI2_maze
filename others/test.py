a=int(input())
list1=list(map(int,input().split())
max=list1[0]
maxi=0
for i in range(0,a):
    if(max<list1[i]):
        max=list1[i]
        maxi=i
print("{:} {:}".format(max,maxi))5