import java.util.Arrays;

public class One {
    public int[] twoSum(int[] nums, int target) {
        int[] newArray = new int[nums.length];
        System.arraycopy(nums, 0, newArray, 0, nums.length);
        Arrays.sort(nums);

        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            if (nums[left] + nums[right] == target) {
                break;
            } else if (nums[left] + nums[right] > target) {
                right -= 1;
            } else {
                left += 1;
            }
        }
        int leftValue = nums[left];
        int rightValue = nums[right];

        for (int i = 0; i < nums.length; i++) {
            if (newArray[i] == leftValue) {
                left = i;
            } else if (newArray[i] == rightValue) {
                right = i;
            }
        }

        return new int[]{left, right};
    }
}
