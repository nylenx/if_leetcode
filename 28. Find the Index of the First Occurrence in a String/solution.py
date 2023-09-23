class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = -1
        for i in range(0,len(haystack)):
            try:
                # print(i,haystack[i:i+len(needle)])
                if haystack[i:i+len(needle)] == needle:
                    return i
            except:
                return -1
        return output