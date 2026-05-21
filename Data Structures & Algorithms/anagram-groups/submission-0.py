class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs:
            sorted_s = "".join(sorted(str))

            # group them using a hashmap
            if sorted_s not in groups:
                groups[sorted_s] = []
            
            groups[sorted_s].append(str)

        return list(groups.values())