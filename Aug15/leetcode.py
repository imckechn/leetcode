class Solution:
    def findSubstring(s, words):
        substringIndexes = []
        iterationAmount = len(words[0])
        lenS = len(s)
        wordCount = len(words)

        i = 0
        while(i <= lenS - (iterationAmount * wordCount)):
            wordsDic = {}
            success = False
            for j in range(i, i + iterationAmount * wordCount, iterationAmount):
                success = True
                wordBeingChecked = s[j:j + iterationAmount]
                if wordBeingChecked in words and words.count(wordBeingChecked) > list(wordsDic.keys()).count(wordBeingChecked):
                    wordsDic[wordBeingChecked] = j

                    if wordCount == len(wordsDic):
                        j = i
                        break

                else:
                    success = False
                    if wordBeingChecked not in words:
                        i = j

                    elif ((wordBeingChecked in wordsDic.keys())):
                        i = wordsDic[wordBeingChecked]

                    break
                    
            if success:
                substringIndexes.append(i)
                i = j
            
            i += iterationAmount

        return substringIndexes
                    

# print(Solution.findSubstring('barfoothefoobarman', ['foo', 'bar'])) #[0,9]
# print(Solution.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"])) #[]
# print(Solution.findSubstring('barfoofoobarthefoobarman', ["bar","foo","the"])) #[6, 9, 12]
print(Solution.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","good"])) #[8]