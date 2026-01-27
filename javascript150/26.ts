function removeDuplicates(nums: number[]): number {
    var newList: Array<number> = [nums[0]];
    for (var i = 1; i < nums.length; i++) {
        if (nums[i] != newList[newList.length-1]) {
            newList.push(nums[i]);
        }
    }

    for (var i = 0; i < newList.length; i++) {
        nums[i] = newList[i];
    }

    return newList.length;
};

removeDuplicates([1,1,2])