class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        title_len = len(columnTitle)
        for i in range(title_len):
            output = output + ((ord(columnTitle[i])-64)*(26**(title_len-1-i)))
        return output