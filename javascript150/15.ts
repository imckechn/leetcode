function threeSum(nums: number[]): number[][] {
    nums = nums.sort((a, b) => a-b)
    let answer: number[][] = []

    for (let a = 0; a < nums.length-1; a++) {
        if (a > 0 && nums[a] === nums[a - 1]) continue;
        let left = a+1, right = nums.length-1

        while (left < right) {
            let total = nums[a] + nums[left] + nums[right]

            if (total < 0) {
                left++
            } else if (total > 0) {
                right--
            } else {
                let ans = [nums[a], nums[left], nums[right]].sort((a,b)=>a-b)
                answer.push(ans)

                left++
                while (left < right && nums[left] == ans[1]) {
                    left++
                }

                right--
                while (left < right && nums[right] == ans[2]) {
                    right--
                }
            }
        }
    }
    return answer;
};

console.log(threeSum([-1,0,1,2,-1,-4]))