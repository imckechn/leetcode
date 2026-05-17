class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;

        while (i < nums.length-1) {
            if (nums[i] == nums[i+1]) {
                for (int j = i+2; j < nums.length; j++) {
                    if (nums[i+j] == "") {
                        nums[i+j-1] = "";
                        break;
                    }
                    nums[i+j-1] = nums[i+j];
                }
                nums[nums.length-1] = ""

            } else {
                i = i+1;
            }
        }
        return nums.length;
    }
}