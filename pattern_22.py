class Solution():
    def pattern_22(self,N):
        for i in range(N):
            for j in range(N):
                if i==0 or j==0 or i==N-1 or j==N-1:
                    print("4",end="")
                elif i==1 or j==1 or i==N-2 or j==N-2:
                    print("3",end="")
                elif i==2 or j==2 or i==N-3 or j==N-3:
                    print("2",end="")
                else:
                    print("1",end="")
            print()
if __name__=="__main__":
    sol=Solution()
    N=7
    sol.pattern_22(N)