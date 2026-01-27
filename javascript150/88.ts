/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    var j: number = 0;
    for (var i = m; i < n+m; i++) {
        nums1[i] = nums2[j];
        j += 1;
    }

    nums1.sort((a: any, b: any) => a-b);
};

merge([1], 1, [], 0)
merge([1,2,3,0,0,0], 3, [2,5,6], 3)