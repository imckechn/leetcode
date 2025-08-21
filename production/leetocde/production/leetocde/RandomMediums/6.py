'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''


# Need to write this in two parts. One to create the array in the zigzag patter,
# Other to print out said array

def populateFullColumn(zigzag, input):
    for i in range(len(zigzag)):
        if len(input) == 0:
            break

        zigzag[i] += input[0]
        input = input[1:]

    return zigzag, input


def populateSingleValue(zigzag, input, column):
    for i in range(len(zigzag)):
        if i == column:
            zigzag[i] += input[0]
            input = input[1:]
        else:
            zigzag[i] += " "

    return zigzag, input

def createZigZagArray(input, numRows):
    zigzag = [""] * numRows
    column = 0

    while input:
        if column % (numRows - 1) == 0:
            zigzag, input = populateFullColumn(zigzag, input)

        else:
            zigzag, input = populateSingleValue(zigzag, input, column )

        column += 1
        if column == numRows - 1:
            column = 0

    return zigzag


def getZigZagList(array):
    ans = ""

    for row in array:
        for char in row:
            if char != " ":
                ans += char

    return ans

def stringZigzag(input, numRows) -> list:
    array = createZigZagArray(input, numRows)
    return getZigZagList(array)



def testRunner():

    # print("\nTest 1")
    # correct = "PAHNAPLSIIGYIR"
    # ans = stringZigzag("PAYPALISHIRING", 3)
    # if ans == correct:
    #     print("Correct")
    # else:
    #     print("Failed, Expected ", correct, ", got ", ans)

    print("\nTest 2")
    correct = "PINALSIGYAHRPI"
    ans = stringZigzag("PAYPALISHIRING", 4)
    if ans == correct:
        print("Correct")
    else:
        print("Failed, Expected ", correct, ", got ", ans)

    print("\nTest 3")
    correct = "PAYPALISHIRING"
    ans = stringZigzag("PAYPALISHIRING", 1)
    if ans == correct:
        print("Correct")
    else:
        print("Failed, Expected ", correct, ", got ", ans)

    print("\nTest 4")
    correct = "A"
    ans = stringZigzag("A", 1)
    if ans == correct:
        print("Correct")
    else:
        print("Failed, Expected ", correct, ", got ", ans)
    
testRunner()