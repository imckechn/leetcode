class Solution:
    def simplifyPath(path):
        dir = path.split("/")
        ans = []

        for i in range(len(dir)):
            if dir[i] != "." and dir[i] != "":
                if dir[i] == "..":
                    if len(ans) != 0:
                        ans.pop(-1)
                else:
                    ans.append(dir[i])

        if len(ans) == 0:
            return "/"

        output = "/"
        for elem in ans:
            output += elem + "/"

        return output[:-1]

# print(Solution.simplifyPath("/home/"))
# print(Solution.simplifyPath("/home//foo/"))
# print(Solution.simplifyPath("/home/home/home/home/"))
# print(Solution.simplifyPath("/home/user/Documents/../Pictures"))
# print(Solution.simplifyPath("/home/../Documents/../Pictures"))
print(Solution.simplifyPath("/../"))
# print(Solution.simplifyPath("/a/./b/../../c/"))
# print(Solution.simplifyPath("/a/../../b/../c//.//"))
# print(Solution.simplifyPath("/a//b////c/d//././/.."))
print(Solution.simplifyPath("/home/foo/./.././bar"))
