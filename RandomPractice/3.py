class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        found = set(s[0])
        left = 0
        right = 1
        largest = 1


        while right < len(s):
            if s[right] in found:
                
                while s[left] != s[right]:
                    found.remove(s[left])
                    left += 1

                left += 1

            else:
                found.add(s[right])

            largest = max(largest, right-left + 1)
            right += 1

        return largest

sol = Solution()
print(sol.lengthOfLongestSubstring("au"))