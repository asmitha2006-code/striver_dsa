class Solution:
    def pattern_13(self,N):
        start=1
        for i in range(N):
            for j in range(i+1):
                print(start,end=" ")
                start+=1
            print()
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_13(N)