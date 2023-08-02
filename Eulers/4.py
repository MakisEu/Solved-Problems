def is_pallindome(number):
    num_to_string=str(number)
    n=len(num_to_string)
    for i in range(n//2):
        if (num_to_string[i]!=num_to_string[n-1-i]):
            return False
    return True
#m=999
#n=999
flag=True
max=0
for i in range(999,500,-1):
    for j in range(999,500,-1):
        if (is_pallindome(i*j)):
            #print("m={0},n={1},P]{2}".format(i,j,i*j))
            if (max<i*j):
                max=i*j
print (max)
#while (m>90 and n>98):
 #   if (is_pallindome(m*n)):
  #      print("m={0},n={1},P]{2}".format(m,n,m*n))
   #     break
    #if (m>n):
     #   m-=1
    #else:
#    n-=1
