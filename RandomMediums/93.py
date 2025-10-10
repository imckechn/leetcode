from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]: 
        return Solution.backtrackIp(s, 0)


    def backtrackIp(s, index):
        #base case
        if index == 3:
            if Solution.validateIp(s):
                return [s]
            else:
                return []
        foundIps = []

        s = Solution.addPeriod(s, index)

        ans = Solution.backtrackIp(s, index + 1)
        if ans != []:
            foundIps += ans


        for i in range(2):
            s = Solution.updatePeriod(s)

            ans = Solution.backtrackIp(s, index + 1)
            if ans != []:
                foundIps += ans

        s = Solution.popPeriod(s)
        return foundIps


    def validateIp(s):
        ints = []
        lastPeriod = 0
        for i in range(len(s)):
            if s[i] == ".":
                ints.append(s[lastPeriod:i])
                lastPeriod = i+1
        ints.append(s[lastPeriod:])
        
        for i in ints:
            if len(i) > 1 and i[0] == "0":
                return False
            if len(i) > 3 or len(i) == 0:
                return False
            if int(i) > 255:
                return False

        return True

    def popPeriod(s):
        i = len(s)
        j = i-1

        for j in range(i-1, -1, -1):
            if s[j] == ".":
                break

        return s[:j] + s[j+1:]

    def addPeriod(s, index):
        count = 0
        i = 0

        for i in range(len(s)):
            if s[i] == ".":
                count += 1

            elif count == index:
                break

        s = s[:i+1] + "." + s[i+1:]

        return s
 
    def updatePeriod(s):
        i = len(s)
        j = i-1

        for j in range(i-1, -1, -1):
            if s[j] == ".":
                break

        s = s[:j] + s[j+1:]

        s = s[:j+1] + "." + s[j+1:]

        return s



#First  
ans = ["255.255.11.135","255.255.111.35"]
result = Solution.restoreIpAddresses(None, "25525511135")

if ans == result:
    print("1: Success")
else:
    print("1: Failure, got " + str(result))


#Second  
ans = ["0.0.0.0"]
result = Solution.restoreIpAddresses(None, "0000")

if ans == result:
    print("2: Success")
else:
    print("2: Failure, got " + str(result))


#Third  
ans = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
result = Solution.restoreIpAddresses(None, "101023")

if ans == result:
    print("3: Success")
else:
    print("3: Failure, got " + str(result))