class Solution:
    def pattern_17(self,N):
        for i in range(N):
            print(" " * (N-i-1),end="")

            ch=ord('A')
            breakpoint=(2*i + 1)//2

            for j in range(1,2*i+2):
                print(chr(ch),end="")
                if j<=breakpoint:
                    ch+=1
                else:
                    ch-=1
            print()
if __name__=="__main__":
    sol=Solution()
    N=4
    sol.pattern_17(N)
                


