class Solution:
    def pattern_2(self,N):
        for i in range(N):
            print("*" * (i+1))
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_2(N)
