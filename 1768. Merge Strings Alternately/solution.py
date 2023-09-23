class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range(0,len(word1)):
            try:
                merged = merged + word1[i] + word2[i]
            except:
                merged = merged + word1[i]
        merged = merged + word2[len(word1): len(word2)+1]
        return merged