class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            try:
                if c == s[i]:
                    i+=1
            except:
                continue
        return True if i == len(s) else False
        