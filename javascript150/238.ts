function productExceptSelf(nums: number[]): number[] {
    let left = [1]
    let right = [1]
    let answer = []
    
    let product = 1
    for (let i = nums.length-1; i >= 0; i--) {
        product *= nums[i]
        left.splice(0,0,product)
    }

    product = 1;
    for (let i = 0; i < nums.length; i++) {
        product *= nums[i]
        right.push(product)
    }

    for (let i = 0; i < nums.length; i++) {
        answer.push(left[i+1] * right[i])
    }

    return answer;
};

console.log(productExceptSelf([1, 2, 3, 4]))
                            //[24,12,8, 6]