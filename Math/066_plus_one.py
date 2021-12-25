class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = int("".join([str(i) for i in digits]))
        i += 1
        return [int(j) for j in str(i)]
