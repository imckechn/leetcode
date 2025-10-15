class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = ""
        for i in range(max(len(word1), len(word2))):
            if len(word1) > i:
                combined += word1[i]
            if len(word2) > i:
                combined += word2[i]
        return combined
    
#Q1
word1 = "abc"
word2 = "pqr"
ans = "apbqcr"

ret = Solution.mergeAlternately(None, word1, word2)
if ret == ans:
    print("Q1: Passed")
else:
    print("Q1: failed " + ret)


#Q2
word1 = "ab"
word2 = "pqrs"
ans = "apbqrs"

ret = Solution.mergeAlternately(None, word1, word2)
if ret == ans:
    print("Q2: Passed")
else:
    print("Q2: failed " + ret)


#Q3
word1 = "abcd"
word2 = "pq"
ans = "apbqcd"

ret = Solution.mergeAlternately(None, word1, word2)
if ret == ans:
    print("Q3: Passed")
else:
    print("Q3: failed " + ret)
