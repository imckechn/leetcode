class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return -1
        
        count = 0
        
        if dividend > 0:
            if divisor > 0:
                while dividend >= divisor:
                    dividend -= abs(divisor)
                    count += 1
            
            else:
                while dividend >= abs(divisor):
                    dividend += divisor
                    count -= 1

        else:
            if divisor > 0:
                while abs(dividend) >= divisor:
                    dividend += divisor
                    count -= 1
            
            else:
                while abs(dividend) >= abs(divisor):
                    dividend -= divisor
                    count += 1

        return count
    

sol = Solution()
sol.divide(1, 1)

sol.divide(-7, 3)
sol.divide(-7, -3)