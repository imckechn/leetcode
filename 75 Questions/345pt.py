class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        found = []

        for letter in s:
            if letter in vowels:
                found.append(letter)

        pointer = len(found)-1
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = found[pointer]
                pointer -= 1

        return "".join(s)