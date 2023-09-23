class Solution:
    def findWords(self, words: List[str]) -> List[str]:
            row1 = "qwertyuiop"
            row2 = "asdfghjkl"
            row3 = "zxcvbnm"

            output = []
            for word in words:
                if set(word.lower()).issubset(set(row1)) or set(word.lower()).issubset(set(row2)) or set(word.lower()).issubset(set(row3)):
                    output.append(word)
            return output