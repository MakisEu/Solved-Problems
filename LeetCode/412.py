class Solution:
    def fizzBuzz(self, n):
        answer=[]
        for i in range(min(2,n)):
            answer.append(str(i+1))
        for i in range(3,n+1,1):
            if (i%3==0 and i%5==0):
                s="FizzBuzz"
            elif (i%3==0):
                s="Fizz"
            elif (i%5==0):
                s="Buzz"
            else:
                s=str(i)
            answer.append(s)
        return answer
