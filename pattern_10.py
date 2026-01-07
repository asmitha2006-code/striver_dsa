class Solution:
    def pattern_10(self,N):
        for i in range(N):
            print("*" * (i+1))
        for j in range(N-1,0,-1):
            print("*" * j)
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_10(N)