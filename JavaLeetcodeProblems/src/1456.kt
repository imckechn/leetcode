class Solution1456 {
    fun maxVowels(s: String, k: Int): Int {
        val str = s.lowercase()

        var maxFound = 0
        val vowels = arrayOf('a', 'e', 'i', 'o', 'u')
        var count = 0
        var rightPointer = k-1
        var leftPointer = 0

        for (i in 0..k-1) {
            if (str[i] in vowels)  {
                count++
            }
        }

        maxFound = count
        if (maxFound == k) {
            return maxFound
        }

        while (rightPointer < str.length - 1) {
            if (str[leftPointer] in vowels) {
                count--
            }

            if (str[rightPointer+1] in vowels) {
                count ++
            }

            leftPointer++
            rightPointer++

            if (count > maxFound) {
                maxFound = count
            }
        }

        return maxFound
    }
}


fun main() {
    var str = "abciiidef"
    var expected = 3
    var answer = Solution1456().maxVowels(str, 3)

    if (answer != expected) {
        println("Test 1: Failed (expected $expected, got $answer)")

    } else {
        println("Test 1: Passed")
    }
}