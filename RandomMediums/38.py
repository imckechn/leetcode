class Solution:
    def countAndSay(self, n: int) -> str:
        return ''.join(Solution.countAndSayString(n))

    def countAndSayString(n):
        if n == 1:
            return ["1"]
        
        values = Solution.countAndSayString(n-1)

        count = 1
        current = values[0]
        newValues = []

        for i in range(1, len(values)):
            if values[i] == current:
                count += 1

            else:
                newValues.append(str(count))
                newValues.append(current)
                count = 1
                current = values[i]

        newValues.append(str(count))
        newValues.append(current)

        return newValues

print(Solution.countAndSay(None, 1))
print(Solution.countAndSay(None, 5))

