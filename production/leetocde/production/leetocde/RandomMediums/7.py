class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))

        isNeg = False

        if x[0] == '-':
            x.pop(0)
            isNeg = True
        
        ans = []
        for elem in x:
            ans.insert(0, elem)


        #check if outside the 32signed/unsigned range
        numberBoundry = ''
        if isNeg:
            numberBoundry = list('2147483648')
        else:
            numberBoundry = list('2147483647')

        if len(ans) > len(numberBoundry):
            return 0
        elif len(ans) == len(numberBoundry):    
            for i in range(len(ans)):
                if numberBoundry[i] > ans[i]:
                    break
                if numberBoundry[i] < ans[i]:
                    return 0
                
        if isNeg:
            ans.insert(0, '-')

        return int(''.join(ans))
    
sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))