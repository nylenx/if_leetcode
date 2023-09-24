class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for e in operations:
            if '+' in e:
                output += 1
            else:
                output -= 1
        return output