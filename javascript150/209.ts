function minSubArrayLen(target: number, nums: number[]): number {
    let res = Number.MAX_SAFE_INTEGER;
    let left = 0
    let sum = 0;

    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum >= target) {
            res = Math.min(res, right - left + 1);
            left += 1;
            sum -= nums[left - 1];
        }
    }


    return res === Number.MAX_SAFE_INTEGER ? 0 : res;
};

console.log(minSubArrayLen(11, [1,2,3,4,5])) //3
console.log(minSubArrayLen(4, [1,4,4])) //1
console.log(minSubArrayLen(7, [2,3,1,2,4,3]))