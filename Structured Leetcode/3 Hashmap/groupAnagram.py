class Solution:
    def groupAnagrams(strs):
        groups = []
        anagrams = []

        for word in strs:
            wrd = {}
            for char in word:
                if char in wrd.keys():
                    wrd[char] += 1
                else:
                    wrd[char] = 1

            if wrd in anagrams:
                groups[anagrams.index(wrd)].append(word)
            else:
                anagrams.append(wrd)
                groups.append([word])

        return groups
        

print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))