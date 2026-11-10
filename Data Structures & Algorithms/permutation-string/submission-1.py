class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        window_freq = [0] * 26

        for char in s1:
            idx = ord(char) - ord('a')
            freq[idx] += 1

        for i in range(len(s1)):
            val = s2[i]
            idx = ord(val) - ord('a')
            window_freq[idx] += 1

        if freq == window_freq:
            return True

        for left in range(len(s2) - len(s1)):
            leaving = s2[left]
            entering = s2[left + len(s1)]

            leaving_idx = ord(leaving) - ord('a')
            entering_idx = ord(entering) - ord('a')

            window_freq[leaving_idx] -= 1
            window_freq[entering_idx] += 1

            if freq == window_freq:
                return True

        return False