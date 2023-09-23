class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict = {}
        if len(s) != len(t):
            return False
        for i in range(0,len(s)):
            if count_dict.get(s[i].lower()) is None:
                count_dict[s[i].lower()] = 1
            else:
                count_dict[s[i].lower()] = count_dict[s[i].lower()] + 1

            if count_dict.get(t[i].lower()) is None:
                count_dict[t[i].lower()] = -1
            else:
                count_dict[t[i].lower()] = count_dict[t[i].lower()] - 1
        return all([True if value==0 else False for value in count_dict.values()] )