function minSubArrayLen(target: number, nums: number[]): number {
    if (target == 0) {
        return 0;
    }
    nums = nums.sort((a,b) => a-b)
    let smallest = Infinity;
    let left = 0, right = 0, total = nums[0];

    while (left <= right && right < nums.length) {
        if (total < target) {
            right += 1
            total += nums[right]
        
        } else if (total > target) {
            total -= nums[left]
            left += 1
        
        } else {
            if (left == right) {
                return 1
            }
            smallest = Math.min(smallest, right-left)
            right += 1
        }
    }

    if (smallest == Infinity) {
        return 0;
    } else {
        return smallest
    }
};

console.log(minSubArrayLen(11, [1,2,3,4,5]))
console.log(minSubArrayLen(4, [1,4,4]))
console.log(minSubArrayLen(7, [2,3,1,2,4,3]))