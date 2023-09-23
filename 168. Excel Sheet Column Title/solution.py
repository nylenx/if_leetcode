class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber >0 :
            output = chr(((columnNumber-1)%26)+65) + output 
            columnNumber = (columnNumber-1) // 26
        return output