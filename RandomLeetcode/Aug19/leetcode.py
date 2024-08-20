class Solution:

    def isHappy(n):
        foundNumbers = []

        while True:
            if n == 1:
                return True

            n = str(n)
            arr = []
            for char in n:
                arr.append(int(char))

            sum = 0
            for num in arr:
                sum += num * num

            if sum in foundNumbers:
                return False
            

            foundNumbers.append(sum)
            n = sum
    
print(Solution.isHappy(31))