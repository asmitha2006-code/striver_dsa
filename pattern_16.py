class Solution:
    def pattern_16(self,N):
        for i in range(N):
            for j in range(i+1):
                print(chr(65+i),end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_16(N)