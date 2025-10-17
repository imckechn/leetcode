class Solution1679 {
    fun maxOperations(nums: IntArray, k: Int): Int {
        nums.sort()

        var p1 = 0
        var p2 = nums.size - 1
        var count = 0

        while(p1 < p2) {
            if (nums[p1] + nums[p2] == k) {
                count++
                p1++
                p2--
            } else if (nums[p1] + nums[p2] < k) {
                p1++
            } else if (nums[p1] + nums[p2] > k) {
                p2--
            }
        }
        return count
    }
}


fun main() {

    //Test 1
    var input: IntArray = intArrayOf(1,2,3,4)
    var expected = 2
    var answer = Solution1679().maxOperations(input, 5)

    if (answer != expected) {
        println("Test 1: Failed (expected $expected, got $answer)")

    } else {
        println("Test 1: Passed")
    }


    //Test 2
    input = intArrayOf(3,1,3,4,3)
    expected = 1
    answer = Solution1679().maxOperations(input, 6)

    if (answer != expected) {
        println("Test 2: Failed (expected $expected, got $answer)")

    } else {
        println("Test 2: Passed")
    }
}