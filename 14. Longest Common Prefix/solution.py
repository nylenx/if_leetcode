class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_str = ""
        for i in range(0,len(strs[0])):
            for el in strs[1:len(strs)]:
                # print(el,len(el),i)
                if len(el) > i:
                    if el[i] != strs[0][i]:
                        return common_str
                else:
                    return common_str
            else:
                common_str = common_str + strs[0][i]
        return common_str