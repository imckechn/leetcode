from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True

        options = []
        for word in wordDict:
            if word == s[:len(word)]:
                options.append(word)

        for option in options:
            ans =  Solution.wordBreak(self, s[len(option):], wordDict)

            if ans == True:
                return True
            
        return False
    

print(Solution.wordBreak(None, "leetcode", ['leet', 'code']))