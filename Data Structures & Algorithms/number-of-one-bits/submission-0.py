class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)[2:]
        total = 0
        for i in num:
            if i == '1':
                total = total + 1

        return total