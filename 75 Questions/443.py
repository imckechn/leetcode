from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []

        currentCharater = chars[0]
        length = 0
        for char in chars:
            if char == currentCharater:
                length += 1

            else:
                s.append(currentCharater)
                currentCharater = char

                if length > 1:
                    for c in str(length):
                        s.append(c)
                    length = 1

        s.append(currentCharater)
        currentCharater = char

        if length > 1:
            for c in str(length):
                s.append(c)
                length = 1

        chars[:] = s
        return len(chars)

sol = Solution()
sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])