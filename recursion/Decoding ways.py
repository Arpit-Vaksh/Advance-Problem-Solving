class Solution:
    def numDecodings(self, s: str) -> int:
        dp =[-1 for i in range(len(s))]

        if len(s)==0:
            return 0
        return self.solve(s,0,dp)

    def solve(self,s,i,dp):
        if i==len(s):
            return 1
        if s[i]=='0':
            return 0
        if dp[i] != -1:
            return dp[i]
        left = self.solve(s,i+1,dp)
        right=0
        if (i+1 < len(s) and s[i]=='1') or (i+1 < len(s) and s[i]=='2' and s[i+1] < '7'):
            right = self.solve(s,i+2,dp)
        ans=left+right
        dp[i]=ans
        return ans
