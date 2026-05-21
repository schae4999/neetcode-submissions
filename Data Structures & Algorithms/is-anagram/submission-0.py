class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap - frequency and keys should match
        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 0
            hm[i] = hm[i] + 1
        
        for j in t:
            if j not in hm:
                return False
            hm[j] = hm[j] - 1
        
        for a in hm:
            if hm[a] != 0:
                return False
        return True