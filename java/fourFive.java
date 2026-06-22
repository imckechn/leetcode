import java.util.ArrayList;

public class fourFive {
    public int jump(int[] nums) {
        if (nums.length == 0 || nums.length == 1) {
            return 0;
        }

        int currentIndex = 0;
        ArrayList<Integer> jumpLocations = new ArrayList<>();
        jumpLocations.add(0);

        while (currentIndex != nums.length-1) {
            if (currentIndex+nums[currentIndex]+1 >= nums.length) break;

            int furthestJump = 0;
            int indexOfJump = 0;
            for (int i = currentIndex+1; i < nums[currentIndex] + currentIndex+1; i++) {
                if (furthestJump <= nums[i] + i) {
                    indexOfJump = i;
                    furthestJump = nums[i] + i;
                }
            }
            currentIndex = indexOfJump;
            jumpLocations.add(indexOfJump);
        }

        return jumpLocations.size();
    }
}
