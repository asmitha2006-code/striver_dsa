class Solution:
    def pattern_8(self,N):
        for i in range(N):
            for j in range(N-1,N-i-1,-1):
                print(" ",end="")
            for j in range(2*(N-i-1)+1):
                print("*",end="")
            for j in range(N-1,N-i-1,-1):
                print(" ",end="")
            print()

if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_8(N)
            