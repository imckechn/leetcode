class Solution:
    def simplifyPath(path):
        dir = path.split("/")

        i = 0
        output = "/"
        while i < len(dir):
            if dir[i] == "" or dir[i] == ".":
                dir.pop(i)
            elif dir[i] == ".." and i > 0:
                dir.pop(i)
                dir.pop(i-1)
                i -= 1
            elif dir[i] == "..":
                dir.pop(i)
            elif i+1 < len(dir) and dir[i+1] == "..":
                dir.pop(i+1)
                dir.pop(i)

                if i != 0:
                    i -= 1
            else:
                i += 1

        output = "/"
        for elem in dir:
            output += elem + "/"

        if output == "/":
            output = "//"
        return output[:-1]

# print(Solution.simplifyPath("/home/"))
# print(Solution.simplifyPath("/home//foo/"))
# print(Solution.simplifyPath("/home/home/home/home/"))
# print(Solution.simplifyPath("/home/user/Documents/../Pictures"))
# print(Solution.simplifyPath("/home/../Documents/../Pictures"))
# print(Solution.simplifyPath("/../"))
# print(Solution.simplifyPath("/a/./b/../../c/"))
# print(Solution.simplifyPath("/a/../../b/../c//.//"))
# print(Solution.simplifyPath("/a//b////c/d//././/.."))
print(Solution.simplifyPath("/home/foo/./.././bar"))
