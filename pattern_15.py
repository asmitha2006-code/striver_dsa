class Solution:
    def pattern_15(self,N):
        for i in range(N):
            for j in range(N-i):
                print(chr(65+j),end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_15(N)
