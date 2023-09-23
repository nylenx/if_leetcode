import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanu_string = "".join([str(i) for i in [x.lower() for x in s if x.isalnum()]])

        rstring = alphanu_string[::-1]
        mid = math.ceil(len(alphanu_string)/2)
        for i in range(0,mid):
            if alphanu_string[i] != rstring[i]:
                return False
        else:
            return True