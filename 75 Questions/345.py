class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        left = 0
        right = len(s)-1

        vowels = [
            'a',
            'A',
            'e',
            'E',
            'i',
            'I',
            'o',
            'O',
            'u',
            'U',
        ]

        while left < right:
            if string[left] in vowels and string[right] in vowels:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1

            elif string[left] in vowels:
                right -= 1

            elif string[right] in vowels:
                left += 1

            else:
                left += 1
                right -= 1
        return ''.join(string)

sol = Solution()
sol.reverseVowels("Ui")