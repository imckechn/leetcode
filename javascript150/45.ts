function jump(nums: number[]): number {
    if (nums.length <= 1) {
        return 0
    }

    var mostJumps = 0;
    var nextPos = 0;
    for (let i = 1; i <= nums[0]; i++) {
        if (nums[i] + i > mostJumps) {
            nextPos = i;
            mostJumps = nums[i] + i;
        } else if (nums[i] + i >= nums.length) {
            return 1;
        }
    }
    return jump(nums.slice(nextPos)) + 1;
};

console.log(jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
console.log(jump([2,3,1,1,4]))
console.log(jump([1,2]))