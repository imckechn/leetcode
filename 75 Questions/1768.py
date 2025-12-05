class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        len1 = len(word1)
        len2 = len(word2)
        smallest = min(len1, len2)

        for i in range(smallest):
            answer += word1[i] + word2[i]

        if len1 > smallest:
            answer += word1[smallest:]
        else:
            answer += word2[smallest:]

        return answer