class Solution:
    def isPalindrome(self, s: str) -> bool:
        # one pointer from the start, one from the end
        s = ''.join(char for char in s if char.isalnum()).lower()

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True