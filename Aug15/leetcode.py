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
            wordsFound = 0
            for j in range(i, i + iterationAmount * wordCount, iterationAmount):
                success = True
                wordBeingChecked = s[j:j + iterationAmount]
                if wordBeingChecked in words and (wordBeingChecked not in wordsDic.keys() or len(wordsDic[wordBeingChecked]) < words.count(wordBeingChecked)):
                    wordsFound += 1
                    if wordBeingChecked in wordsDic.keys() and words.count(wordBeingChecked) < len(wordsDic[wordBeingChecked]):
                        success = False
                        if wordBeingChecked not in words:
                            i = j

                        elif wordBeingChecked in wordsDic.keys():
                            i = wordsDic[wordBeingChecked][0]

                        break

                    elif wordBeingChecked not in wordsDic.keys():
                        wordsDic[wordBeingChecked] = []

                    wordsDic[wordBeingChecked].append(j)

                    if wordCount == wordsFound:
                        j = i
                        break

                else:
                    success = False
                    if wordBeingChecked not in words:
                        i = j

                    elif wordBeingChecked in wordsDic.keys():
                        i = wordsDic[wordBeingChecked][0]

                    break
                    
            if success:
                substringIndexes.append(i)
                i = j
            
            i += iterationAmount

        return substringIndexes
                    

# print(Solution.findSubstring('barfoothefoobarman', ['foo', 'bar'])) #[0,9]
# print(Solution.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"])) #[]
# print(Solution.findSubstring('barfoofoobarthefoobarman', ["bar","foo","the"])) #[6, 9, 12]
# print(Solution.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","good"])) #[8]
print(Solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])) #[13]