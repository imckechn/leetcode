public class threeThree {

    int findPivot(int[] nums) {
        int left = nums[0];
        int current = nums.length/2;

        while (nums[current] > left) {
            current += current/2;
        }

        while (current > 0 && nums[current-1] < nums[current]) {
            current -= current/2;
        }

        return current-1;
    }

    public int search(int[] nums, int target) {
        if (nums[0] == target) return 0;

        int pivotIndex = findPivot(nums);
        int left, right;
        if (pivotIndex == -1) {
            left = 0;
            right = nums.length -1;
        } else {
            if (nums[0] <= target && nums[pivotIndex] >= target) {
                left = 0;
                right = pivotIndex;

            } else if (nums[pivotIndex+1] <= target && nums[nums.length-1] >= target) {
                left = pivotIndex+1;
                right = nums.length-1;

            } else {
                return -1;
            }
        }
        
        int current = left + (right-left)/2;

        while (nums[current] != target) {
            if (nums[current] > target) {
                right = current;
            } else {
                left = current;
            }

            current = left + (right-left)/2;
        }
        
        return current;
    }
}
