function canJump(nums: number[]): boolean {
    if (nums.length <= 1) {
        return true;
    }

    var maxJump: number = nums[0]-1;
    var i: number = 1;

    while (maxJump >= 0) {
        maxJump -= 1;
        if (i == nums.length-1) {
            return true;
        }

        if (nums[i] > maxJump) {
            maxJump = nums[i]-1;
        }

        i += 1;
    }

    return false;
};