class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        length = len(s)
        mid = length//2
        for thing in range(mid):
            if s[thing] == s[length - thing - 1]:
                continue
            else:
                return False
        return True


        