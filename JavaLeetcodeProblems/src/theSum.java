import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class theSum {
    public List<List<Integer>> threeSum(int[] nums) {
        nums = Arrays.stream(nums).sorted().toArray();
        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            int left = i + 1;
            int right = nums.length-1;

            while (left < right) {
                if (nums[i] + nums[left] + nums[right] == 0) {
                    if (!answer.contains(List.of(nums[i], nums[left], nums[right]))) {
                        answer.add(List.of(nums[i], nums[left], nums[right]));
                    }
                    left += 1;

                } else if (nums[i] + nums[left] + nums[right] > 0) {
                    right -= 1;

                } else {
                    left += 1;
                }
            }
        }

        return answer;
    }
}
