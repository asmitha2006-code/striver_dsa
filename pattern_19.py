class Solution():
    def pattern_19(self,N):
        for i in range(N):
                print("*" * (N-i),end="")
                print(" " * (2*i),end="")
                print("*" * (N-i),end="")
                print()
        for j in range(N):
             print("*" * (j+1),end="")
             print(" " * (2*(N-j-1)),end="")
             print("*" * (j+1),end="")
             print()

if __name__=="__main__":
     sol=Solution()
     N=5
     sol.pattern_19(N)