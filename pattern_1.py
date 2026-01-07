class Solution:
    def pattern_1(self,N):
        for i in range(N):
            for j in range(N):
                print("*",end=" ")
            print()
sol=Solution()
N=5
sol.pattern_1(N)