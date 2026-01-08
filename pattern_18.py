class Solution:
    def pattern_18(sef,N):
        for i in range(N):
            for j in range(i+1,0,-1):
                print(chr(65+(N-j)),end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    N=5
    sol.pattern_18(N)
                