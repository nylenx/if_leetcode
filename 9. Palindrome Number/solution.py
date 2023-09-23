import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        rstring_x = str(x)[::-1]
        mid = math.ceil(len(string_x)/2)
        for i in range(0,mid):
            if string_x[i] != rstring_x[i]:
                return False
        else:
            return True
        