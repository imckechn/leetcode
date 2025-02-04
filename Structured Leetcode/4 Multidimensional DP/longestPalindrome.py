class Solution:
    def getPalinRelectLen(s, a, b):
        x = 1

        while a-x >= 0 and b+x+1 < len(s):
            if s[a-x] != s[b+x+1]:
                break
            else:
                x+=1

        return x*2

    def getPalinSiblingsLen(s, i):
        x = 1

        while i+x < len(s) and i-x >= 0:
            if s[i-x] != s[i+x]:
                break
            else:
                x += 1
        return x*2

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        largest = 1
        index = 0
        reflect = False

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                ans = Solution.getPalinSiblingsLen(s, i)
                if ans > largest: 
                    largest = ans
                    index = i
                    

            elif s[i-1] == s[i+1]:
                ans = Solution.getPalinRelectLen(s, i-1, i)
                if ans > largest: 
                    largest = ans
                    index = i
                    reflect = True

        pal = ""

        if reflect:
            for i in range(index - largest//2, index + largest//2 +1):
                pal += s[i]
        else:
            for i in range((index - largest//2)+1, index + largest//2 +1):
                pal += s[i]

        return pal
    

        

print(Solution.longestPalindrome(None, "babad"))
print(Solution.longestPalindrome(None, "cbbd"))
print(Solution.longestPalindrome(None, "qwertyuiopoiuytrewq"))