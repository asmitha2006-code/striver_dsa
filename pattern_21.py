class Solution():
    def pattern_21(self,N):
        for i in range(N):
            for j in range(N):
                if i==0 or j==0 or i==N-1 or j==N-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
if __name__=="__main__":
    sol=Solution()
    N=4
    sol.pattern_21(N)