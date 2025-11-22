class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            num = str(i)

            if '3' in num or '4' in num or '7' in num:
                continue

            for j in range(len(num)):
                if num[j] == '2':
                    num = num[:j] + '5' + num[j+1:]
                elif num[j] == '5':
                    num = num[:j] + '2' + num[j+1:]
                elif num[j] == '6':
                    num = num[:j] + '9' + num[j+1:]
                elif num[j] == '9':
                    num = num[:j] + '6' + num[j+1:]
            if int(num) != i:
                count += 1
        return count
    
sol = Solution()

print(sol.rotatedDigits(10))