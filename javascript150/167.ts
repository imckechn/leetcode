function twoSum(numbers: number[], target: number): number[] {
    let left: number = 0, 
        right:number = numbers.length-1;

    while (left < right) {
        let total = numbers[left] + numbers[right]
        if (total == target) {
            return [left+1, right+1]
        
        } else if (total < target) {
            left += 1;

        } else {
            right -= 1;
        }
    }

    return [0,0]
};