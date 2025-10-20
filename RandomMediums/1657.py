class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word2Letters = {}
        for letter in word2:
            if letter in word2Letters.keys():
                word2Letters[letter] += 1
            else:
                word2Letters[letter] = 1

        
        word1Letters = {}
        for letter in word1:
            if letter in word1Letters.keys():
                word1Letters[letter] += 1
            else:
                word1Letters[letter] = 1

        for key in word2Letters.keys():
            if key not in word1Letters.keys():
                return False

        swapped = {}
        for word2Key in word2Letters.keys():
            found == False

            for word1Key in word1Letters:
                if word2Letters[word2Key] == word1Letters[word1Key]:
                    swapped[word2Key] = word1Key
                    word1Letters[word1Key] = None
                    found = True
                    break

            if not found:
                return found

        for key in word1Letters:
            if word1Letters[key] != None:
                return False

        word2 = list(word2)
        for key in swapped.keys():
            value = swapped[key]

            for i in range(len(word2)):
                if word2[i] == key:
                    word2[i] = value
                    swapped[key] = None
                    break

            else:
                return False

        for key in swapped.keys():
            if swapped[key] != None:
                return False

        return True

#Test 0
expected = False
answer = Solution.closeStrings(None, 'a', 'aa')
if answer == expected:
    print("Q0: Passed")

else:
    print("Q0: Failed, expected " + str(expected) + " but got " + str(answer))

#Test 1
expected = True
answer = Solution.closeStrings(None, 'abc', 'bca')
if answer == expected:
    print("Q1: Passed")

else:
    print("Q1: Failed, expected " + str(expected) + " but got " + str(answer))


#Test 2
expected = True
answer = Solution.closeStrings(None, "cabbba", "abbccc")
if answer  == expected:
    print("Q2: Passed")

else:
    print("Q2:Failed, expected " + str(expected) + " but got " + str(answer))
            

#Test 3
expected = False
answer = Solution.closeStrings(None, "uau", "ssx")
if answer  == expected:
    print("Q3: Passed")

else:
    print("Q3:Failed, expected " + str(expected) + " but got " + str(answer))
            
