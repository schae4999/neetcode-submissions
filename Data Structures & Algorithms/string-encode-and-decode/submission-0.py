class Solution:

    # 2#hi5#hello
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i : j])
            word_start = j + 1
            word_end = word_start + length

            decoded.append(s[word_start : word_end])

            i = word_end



        return decoded
