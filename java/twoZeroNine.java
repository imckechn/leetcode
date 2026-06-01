class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        if (nums.length == 0) { return 0; }
        
        int total = nums[0];
        int left = 0;
        int right = 1;
        int minLength = Integer.MAX_VALUE;

        while (right < nums.length-1) {
            if (total >= target) {

                while (total >= target) {
                    if ((right-left)+1 < minLength) {
                        minLength = (right-left)+1;
                    }

                    total -= nums[left];
                    left += 1;
                }
            }

            if (total < target) {
                right += 1;
                total += nums[right];
            }      
        }

        return minLength == Integer.MAX_VALUE ? 0: minLength;
    }
}