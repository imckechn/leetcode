class Solution:
    def interleave(s1, s2, s3):
        for i in range(len(s3)):
            if len(s1) > 0 and len(s2) > 0 and s1[0] == s3[i] and s1[0] == s2[0]:
                s1Copy = s1.copy()
                s1Copy.pop(0)
                s3Copy = s3[i+1:]
                a = Solution.interleave(s1Copy, s2.copy(), s3Copy)

                if a:
                    return a

                s2Copy = s2.copy()
                s2Copy.pop(0)
                s3Copy2 = s3[i+1:]
                b = Solution.interleave(s1.copy(), s2Copy, s3Copy2)

                if b:
                    return b
                else:
                    return False

            if len(s1) > 0 and s3[i] == s1[0]:
                s1.pop(0)

            elif len(s2) > 0 and s3[i] == s2[0]:
                s2.pop(0)

            else:
                return False
            
        return True

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s3 = list(s3)

        if len(s1) + len(s2) != len(s3):
            return False
        return Solution.interleave(s1, s2, s3)


print(Solution.isInterleave(None, "aabd", "abdc", "aabdabcd")) #true
print(Solution.isInterleave(None, "aabcc", "dbbca", "aadbbcbcac")) #true