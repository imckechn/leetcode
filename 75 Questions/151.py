class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = []
        word = ""
        answer = ""

        for char in s:
            if char != ' ':
                word += char
            else:
                if word != "":
                    wordList.append(word)
                    word = ""

        if word != "":
            wordList.append(word)
        
        wordList.reverse()

        for word in wordList:
            answer += word + " "
        return answer[:-1]


sol = Solution()
sol.reverseWords("the  sky is blue")