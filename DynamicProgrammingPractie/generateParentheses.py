from typing import List


class Solution:
    def subdivide(c): #Once this runs (in brute force) I'll add memoization to this method.
        c = list(c)

        indexes = [[0, len(c)-1]]
        depth = 0
        coordinates = []
        for i in range(len(c)):
            if depth == 0 and c[i] == "(":
                coordinates.append(i)
                depth +=1

            elif depth != 0 and c[i] == "(":
                depth +=1

            elif c[i] == ")":
                depth -= 1

                if depth == 0:
                    coordinates.append(i)

                    if coordinates not in indexes:
                        indexes.append(coordinates)
                    coordinates = []

        answer = []
        for pair in indexes:
            new = list(c.copy())

            new.insert(pair[0], "(")
            new.insert(pair[1] + 1, ")")
            answer.append(''.join(new))

        return answer


    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        par = Solution.generateParenthesis(self, n-1)
        copy = par.copy()

        total = set()
        for c in copy:
            total = total.union(set(Solution.subdivide(c)))

        for p in par:
            if "()" + p not in total:
                total.add("()" + p)
            if p + "()" not in total:
                total.add(p + "()")

        return list(total)
    
# print(Solution.generateParenthesis(None, 1))

print(Solution.generateParenthesis(None, 4))
print(Solution.generateParenthesis(None, 3))
# print(Solution.generateParenthesis(None, 5))

# Solution.subdivide("((()))")
# Solution.subdivide("()()(())(()())")