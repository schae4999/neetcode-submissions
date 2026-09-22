from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_dict = defaultdict(int)

        for char in t:
            freq_dict[char] += 1

        window = defaultdict(int)

        left = 0

        required = len(freq_dict)
        formed = 0

        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            char = s[right]

            window[char] += 1

            if char in freq_dict and window[char] == freq_dict[char]:
                formed += 1

            # Shrink the window
            while formed == required:
                curr_len = right - left + 1

                if curr_len < min_len:
                    min_len = curr_len
                    min_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in freq_dict and window[left_char] < freq_dict[left_char]:
                    formed -= 1

                left += 1
            
        if min_len == float("inf"):
            return ""
        
        return s[min_start : min_start + min_len]



        



