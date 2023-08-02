class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        l=0
        i=0
        rows=[]
        for pp in range(numRows):
            rows.append("")
        decreaseFlag=False
        while(i<n):
            if (not decreaseFlag):
                if (l<numRows):
                    rows[l]=rows[l]+s[i]
                    i+=1
                    l+=1
                if (l==numRows):
                    l=l-1
                    decreaseFlag=True
                    if (numRows==1):
                        l=0
                        decreaseFlag=False
            elif (decreaseFlag):
                if (l>1):
                    rows[l-1]=rows[l-1]+s[i]
                    i+=1
                    l=l-1
                if (l==1):
                    decreaseFlag=False
                    l=l-1
        return ''.join(rows)
