class Solution:
    def pattern_12(self,N):
        for i in range(N):
            for j in range(i+1):
                print(j+1,end="")
            print(" "*(2*(N-(i+1))),end="")
            for k in range(i+1,0,-1):
                print(k,end="")
            print()
                
            
if __name__=="__main__":
    sol=Solution()
    N=4
    sol.pattern_12(N)