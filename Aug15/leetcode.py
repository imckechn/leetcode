class Solution:
    def findSubstring(s, words):
        substringIndexes = []
        iterationAmount = len(words[0])
        lenS = len(s)
        wordCount = len(words)

        i = 0
        while(i <= lenS - (iterationAmount * wordCount)):
            wordsDic = {}
            success = True
            for j in range(i, iterationAmount * wordCount, iterationAmount):
                if s[j:j + iterationAmount] in words and s[j:j + iterationAmount] not in wordsDic.keys():
                    wordsDic[s[j:j + iterationAmount]] = j

                    if wordCount == wordsDic.keys():
                        break

                else:
                    success = False
                    if s[j:j + iterationAmount] not in words:
                        i = j + iterationAmount

                    elif (s[j:j + iterationAmount] in wordsDic.keys):
                        i = wordsDic[s[j:j + iterationAmount]]

                    break

                    
                    
            if success:
                substringIndexes.append(i)
                i = iterationAmount * wordCount
                    

        


print(Solution.findSubstring('barfoothefoobarman', ['foo', 'bar'])) #[0,9]
# print(Solution.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"])) #[]
# print(Solution.findSubstring('barfoofoobarthefoobarman', ["bar","foo","the"])) #[6, 9, 12]