class Solution:
    def canConstruct(ransomNote, magazine):
        foundLetters = {}

        for letter in ransomNote:
            if letter in foundLetters.keys():
                foundLetters[letter] += 1
            else:
                foundLetters[letter] = 1

        for letter in magazine:
            if letter in foundLetters.keys():
                if foundLetters[letter] > 1:
                    foundLetters[letter] -= 1
                else:
                    foundLetters.pop(letter)

        

        if len(foundLetters.keys()) == 0:
            return True
        return False
        

print(Solution.canConstruct("aa", "aab"))
print(Solution.canConstruct("aa", "b"))
print(Solution.canConstruct("ab", "ab"))