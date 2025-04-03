class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        values = Solution.countAndSay(self, n-1)
        values = list(values)

        pointerA = 0
        pointerB = 0
        hitEnd = False
        while pointerB < len(values):
            while values[pointerA] == values[pointerB]:
                pointerB += 1

                if pointerB == len(values):
                    hitEnd = True
                    break

            diff = pointerB - pointerA
            i=0
            while i < diff - 1:
                values.pop(pointerA)
                i += 1

            values.insert(pointerA, str(diff))
            pointerA = pointerB - i + 1
            pointerB = pointerB - i + 2

        if not hitEnd:
            values.insert(len(values) - 1, '1')

        return ''.join(values)

print(Solution.countAndSay(None, 4))

