class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0

        leftPointer = 0
        rightPointer = 0

        found = {s[0]}

        longestLength = 1

        while rightPointer < len(s)-1:
            rightPointer += 1

            if s[rightPointer] in found:

                while (s[leftPointer] != s[rightPointer]):
                    found.remove(s[leftPointer])
                    leftPointer += 1
                leftPointer += 1

            else:
                found.add(s[rightPointer])
                longestLength = max(longestLength, len(found))

        return longestLength