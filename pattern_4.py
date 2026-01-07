class Solution:
    def pattern_4(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(i,end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_4(N)