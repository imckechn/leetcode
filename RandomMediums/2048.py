from cmath import inf


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 10000000):
            number = str(i)
            passed = True
            if "0" in number:
                continue

            for j in range(1, 10):
                if number.count(str(j)) != 0 and number.count(str(j)) != j:
                    passed = False
                    break

            if passed:
                return i
            

print(Solution.nextBeautifulNumber(None, 5))