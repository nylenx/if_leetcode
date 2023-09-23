class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        max = 0
        for i in range(len(s)):
            if s[i] in sub:
                sub = sub[sub.find(s[i])+1:len(sub)] + s[i]
            else:
                sub += s [i]
            # print(s[i],sub)
            max = max if max > len(sub) else len(sub)
        # print(max)
        return max