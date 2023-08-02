class Solution:
    def fib(self, n: int) -> int:
        #Base cases: F(0)=0, F(1)=1
        if (n==0):
            return 0
        Fp=0
        F=1
        #Recursive relation: F(n)=F(n-1)+F(n-2)
        for i in range(2,n+1):
            F,Fp=F+Fp,F
        return F
