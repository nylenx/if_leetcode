class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lw = s.split()
        return len(lw[-1])