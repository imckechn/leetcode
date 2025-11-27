class Solution:
    MIN = 1
    MAX = 26

    def numDecodings(self, s: str) -> int:
        total = 1
        length = len(s)
        pointer = 0

        if s[0] == "0":
            return 0
        elif length == 1:
            return 1

        while pointer < length: 
            if pointer+1 == length and s[pointer] != "0":
                total += 1
                pointer += 1
            elif int(s[pointer]) >= self.MIN and int(s[:pointer+2]) < self.MAX and s[:pointer+1] != "0" and pointer+2 < length and s[pointer+1] != "0":
                total *= 2
                pointer += 2
            elif int(s[pointer]) >= self.MIN and int(s[:pointer+2]) < self.MAX and pointer == length-2  and s[pointer+1] != "0":
                total *= 2
                pointer += 2
            elif pointer+1 < length and s[pointer] == "0" and s[pointer+1] == "0":
                return 0
            elif pointer+2 < length and s[pointer] != "0" and s[pointer+1] != "0" and s[pointer+2] != "0" and pointer+3 == length:
                break
            else:
                pointer += 1
        return total
            

        

sol = Solution()
print(sol.numDecodings("10"))
print(sol.numDecodings("226"))
print(sol.numDecodings("12"))
print(sol.numDecodings("11106"))