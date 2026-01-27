function removeElement(nums: number[], val: number): number {
    nums.sort((a: number, b: number) => a-b);

    var i: number = 0;
    while (i < nums.length) {
        if (nums[i] == val) {
            nums.splice(i, 1);
        } else {
            i += 1;
        }
    }

    return nums.length;
};