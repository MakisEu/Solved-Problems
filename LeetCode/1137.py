class Solution:
    def tribonacci(self, n: int) -> int:
        if (n==0):
            return 0
        #Base cases: T(0)=0,T(1)=1,T(2)=1
        Tpp=0
        Tp=1
        T=1
        for i in range(3,n+1):
            T,Tp,Tpp=T+Tp+Tpp,T,Tp
        return T
