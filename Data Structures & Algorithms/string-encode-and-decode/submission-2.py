class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for s in strs:
            encoded_strs += str(len(s)) + "$"  + s
        return encoded_strs
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i : j])
            decoded_strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded_strs