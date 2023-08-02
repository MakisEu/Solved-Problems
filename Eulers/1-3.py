import math
def multiple3or5():
    set1=set(range(0,1000,3))
    set2=set(range(0,1000,5))
    print (sum(set1.union(set2)))
def fibonnachi():
    f1=0
    f2=1
    fn=[0]
    while (f1+f2<4000000):
        ftemp=f1+f2
        f1=f2
        f2=ftemp
        if (ftemp%2==0):
            fn.append(ftemp)
    print (sum(fn))
def greatestPrimeFactor():
    def isPrime(k,lst):
        for i in lst:
            if (k%i==0):
                return 1
        return 0

    primes=[]
    cnt=0
    i=2
    n=600851475143
    x=int(math.sqrt(n))+1
    while (i<x and n>i):
        if (isPrime(i,primes)==0):
            if (n%i==0):
                n=n/i
            cnt=cnt+1
            primes.append(i)
        if (i==2):
            i=i-1
            primes.pop(0)
        i=i+2
    #i=0
    #p=[]
    #print(len(primes))
    #while (n>primes[i] and i<len(primes)):
     #   print(i,primes[i])
      #  if (n%primes[i]==0):
       #     n=n/primes[i]
        #    p.append(primes[i])
        #i+=1
    #if (len(primes)==i):
     #   print("ended",p)
    print (n)
#greatestPrimeFactor()


