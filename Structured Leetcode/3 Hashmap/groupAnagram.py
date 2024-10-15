class Solution:
    def groupAnagrams(strs):
        grouped = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in grouped:
                grouped[sorted_word].append(word)
            else:
                grouped[sorted_word] = [word]
        return list(grouped.values())           

print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))