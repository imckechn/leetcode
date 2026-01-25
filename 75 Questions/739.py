class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        answer = [0 for i in range(len(temperatures))]

        for index, temp in enumerate(temperatures):
            while len(monoStack) > 0 and monoStack[-1][0] < temp:
                oldTemp, oldIndex = monoStack.pop()
                answer[oldIndex] = index - oldIndex

            monoStack.append([temp, index])

        while len(monoStack) != 0:
            oldTemp, oldIndex = monoStack.pop()
            answer[oldIndex] = 0

        return answer