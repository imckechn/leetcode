/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    k = k%nums.length;
    var rotationPoint: number[] = nums.splice(nums.length-k, k);
    nums = nums.splice(0, 0, ...rotationPoint);
};
