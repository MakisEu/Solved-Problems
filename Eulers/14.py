def collaz(n):
    cnt=0
    if (n==1):
        return 1
    elif (n%2==0):
        cnt+=1
        cnt+=collaz(int(n/2))
    else:
        cnt+=1
        cnt+=collaz(int(3*n+1))
    return cnt
max=0
for i in range(1000000):
    x=collaz(i)
    print (x)
    if (x>max):
        max=x
        m=i
print ("Max",m,"with",max)