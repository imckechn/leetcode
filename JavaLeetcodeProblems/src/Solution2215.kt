import kotlin.math.max

class Solution2215 {
    fun findDifference(nums1: IntArray, nums2: IntArray): List<List<Int>> {
        val numbers1 = nums1.toSet()
        val numbers2 = nums2.toSet()

        val uniqueNumber1 = mutableListOf<Int>()
        val uniqueNumber2 = mutableListOf<Int>()

        var found = hashMapOf<Int, Int>()

        for (num in numbers1) {
            found[num] = 1
        }

        for (num in numbers2) {
            if (found[num] == 1) {
                found[num] = 0

            } else {
                found[num] = 2
            }
        }

        for (key in found.keys) {
            if (found[key] == 1) {
                uniqueNumber1.add(key)
            } else if (found[key] == 2) {
                uniqueNumber2.add(key)
            }
        }

        return listOf(uniqueNumber1, uniqueNumber2)
    }
}


fun main() {
    var input1 = intArrayOf(1,2,3)
    var input2 = intArrayOf(2,4,6)
    var expected = arrayOf(
        intArrayOf(1, 3),
        intArrayOf(4, 6)
    )
    var answer = Solution2215().findDifference(input1, input2)

    if (answer != expected) {
        println("Test 1: Failed (expected $expected, got $answer)")

    } else {
        println("Test 1: Passed")
    }
}