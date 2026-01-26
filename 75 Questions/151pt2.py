class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        lst.reverse()

        answer = ""
        for word in lst:
            if word != "":
                answer += word + " "
        return answer[:-1]