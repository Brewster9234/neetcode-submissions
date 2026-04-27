class Solution:

    def encode(self, strs: List[str]) -> str:
        touse = ""
        for bouse in strs:
            touse += str(len(bouse))+"#"+bouse
        return touse

    def decode(self, s: str) -> List[str]:
        clav = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            clav.append(word)
            i = j + 1 + length
        return clav