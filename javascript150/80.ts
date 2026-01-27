function removeDuplicates(nums: number[]): number {
    var count: number = 1;
    var filtered: number[] = [nums[0]];

    for (var i = 1; i < nums.length; i++) {
        if (nums[i] == filtered[filtered.length-1] && count == 1) {
            filtered.push(nums[i]);
            count += 1;
        } else if (nums[i] != filtered[filtered.length-1]) {
            filtered.push(nums[i]);
            count = 0;
        }
    }

    
    for (var i = 0; i < filtered.length; i++) {
        nums[i] = filtered[i];
    }

    return filtered.length;
};