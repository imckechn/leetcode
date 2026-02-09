function longestConsecutive(nums: number[]): number {
    const numSet = new Set(nums);
    let longest = 0;

    for (const num of numSet) {
        // Only start building a sequence if 'num' is the START
        // (i.e., there is no number one less than it)
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentStack = 1;

            while (numSet.has(currentNum + 1)) {
                currentNum += 1;
                currentStack += 1;
            }

            longest = Math.max(longest, currentStack);
        }
    }

    return longest;
}

console.log(longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])) //expect 5
console.log(longestConsecutive([100,4,200,1,3,2]))