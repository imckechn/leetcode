# class Solution:
    # def interleave(s1, s2, s3):
    #     for i in range(len(s3)):
    #         if len(s1) > 0 and len(s2) > 0 and s1[0] == s3[i] and s1[0] == s2[0]:
    #             s1Copy = s1.copy()
    #             s1Copy.pop(0)
    #             s3Copy = s3[i+1:]
    #             a = Solution.interleave(s1Copy, s2.copy(), s3Copy)

    #             if a:
    #                 return a

    #             s2Copy = s2.copy()
    #             s2Copy.pop(0)
    #             s3Copy2 = s3[i+1:]
    #             b = Solution.interleave(s1.copy(), s2Copy, s3Copy2)

    #             if b:
    #                 return b
    #             else:
    #                 return False

    #         if len(s1) > 0 and s3[i] == s1[0]:
    #             s1.pop(0)

    #         elif len(s2) > 0 and s3[i] == s2[0]:
    #             s2.pop(0)

    #         else:
    #             return False
            
    #     return True

    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     s1 = list(s1)
    #     s2 = list(s2)
    #     s3 = list(s3)

    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #     return Solution.interleave(s1, s2, s3)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lenS1, lenS2, lenS3 = len(s1), len(s2), len(s3)
        if lenS1 + lenS2 != lenS3:
            return False
        
        memo = {} 
        
        def helper(i: int, j: int, k: int) -> bool:
            if k == lenS3:
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = False
            if i < lenS1 and s1[i] == s3[k]:
                ans = ans or helper(i + 1, j, k + 1)
                
            if j < lenS2 and s2[j] == s3[k]:
                ans = ans or helper(i, j + 1, k + 1)
            
            memo[(i, j)] = ans
            return ans
        
        return helper(0, 0, 0)

print(Solution.isInterleave(None, "aabd", "abdc", "aabdabcd")) #true
print(Solution.isInterleave(None, "aabcc", "dbbca", "aadbbcbcac")) #true