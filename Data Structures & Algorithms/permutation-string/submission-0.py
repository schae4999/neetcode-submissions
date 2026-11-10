class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        window_freq = [0] * 26

        # Store frequency count
        for char in s1:
            idx = ord(char) - ord('a')
            freq[idx] += 1

        for left in range(len(s2) - len(s1) + 1):
            window_freq = [0] * 26
            
            for offset in range(len(s1)):
                val = s2[left + offset]
                idx = ord(val) - ord('a')
                window_freq[idx] += 1

            if freq == window_freq:
                return True

        return False