class Solution():
    def pattern_20(self,N):
        for i in range(N):
            print("*" * (i+1),end="")
            print(" " * (2*(N-i-1)),end="")
            print("*" * (i+1),end="")
            print()
        for j in range(N):
            print("*" * (N-j),end="")
            print(" " * (2*j),end="")
            print("*" * (N-j),end="")
            print()
if __name__=="__main__":
     sol=Solution()
     N=5
     sol.pattern_20(N)