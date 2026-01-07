class Solution:
    def pattern_3(self,N):
        for i in range(N):
            for j in range(1,i+2):
                print(j,end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_3(N)