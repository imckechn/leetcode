import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class oneFive {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        
        HashSet<List<Integer>> answer = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (i != 0 && nums[i] == nums[i-1]) continue;
            int left = i+1;
            int right = nums.length-1;

            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                if (total == 0) {
                    answer.add(List.of(nums[i], nums[left], nums[right]));
                    right -= 1;
                
                } else if (total > 0) {
                    right -= 1;
                
                } else {
                    left += 1;
                }
            }
        }

        List<List<Integer>> finalAnswer = new ArrayList<>();

        for (List<Integer> elem: answer) {
            finalAnswer.add(elem);
        }

        return finalAnswer;
    }
}
