class Solution:
    def intToRoman(num):
        num = str(num)
        output = ""

        for i in range(len(num)):
            char = num[i]
            value = int(char) * (10 ** (len(num) - i -1))
            if char != '4' and char != '9':
                while (value > 0):
                    if value - 1000 >= 0:
                        output += "M"
                        value -= 1000
                    elif value - 500 >= 0:
                        output += "D"
                        value -= 500
                    elif value - 100 >= 0:
                        output += "C"
                        value -= 100
                    elif value - 50 >= 0:
                        output += "L"
                        value -= 50
                    elif value - 10 >= 0:
                        output += "X"
                        value -= 10
                    elif value - 5 >= 0:
                        output += "V"
                        value -= 5
                    elif value - 1 >= 0:
                        output += "I"
                        value -= 1

            else:
                if value == 4:
                    output += "IV"
                elif value == 9:
                    output += "IX"
                elif value == 40:
                    output += "XL"
                elif value == 90:
                    output += "XC"
                elif value == 400:
                    output += "CD"
                elif value == 900:
                    output += "CM"
        return output

print(Solution.intToRoman(3749)) #"MMMDCCXLIX":
print(Solution.intToRoman(58)) #"LVIII":
print(Solution.intToRoman(1994)) #"MCMXCIV":