class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        sLength = len(s)

        for char in t:
            if char == s[sPointer]:
                sPointer += 1

                if sPointer == sLength:
                    return True

        return False