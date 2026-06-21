import java.util.List;

public class threeFour {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1,-1};

        if (nums.length == 0) return ans;
        if (nums.length == 1 && nums[0] == target) {
            ans[0] = 0;
            ans[1] = 0;
            return ans;
        }
        
        int left = 0;
        int right = nums.length-1;
        int current = left + (right-left)/2;

        while (left != right) {
            if (nums[current] == target) {
                int leftBoundry = left;
                int rightBoundry = right;

                //Find left boundry
                if (nums[leftBoundry] != target) {
                    int newLeft = left;
                    int newRight = current;
                    int newCurrent = newLeft + (newRight-newLeft)/2;

                    while (!(nums[newCurrent] == target && nums[newCurrent-1] != target)) {
                        if (nums[newCurrent] == target) {
                            newRight = newCurrent;

                        } else {
                            newLeft = newCurrent+1; 
                        }
                        newCurrent = newLeft + (newRight-newLeft)/2;
                    }

                    leftBoundry = newCurrent;
                }

                if (nums[nums.length-1] != target) {
                    int newLeft = current;
                    int newRight = right;
                    int newCurrent = newLeft + (newRight-newLeft)/2;

                    while (!(nums[newCurrent] == target && nums[newCurrent+1] != target)) {
                        if (nums[newCurrent] == target) {
                            newLeft = newCurrent;

                        } else {
                            newRight = newCurrent; 
                        }
                        newCurrent = newLeft + (newRight-newLeft)/2;
                    }

                    rightBoundry = newCurrent;
                }

                ans[0] = leftBoundry;
                ans[1] = rightBoundry;
                return ans ;

            } else if (nums[current] > target) {
                right = current;

            } else {
                left = current+1;
            }

            current = left + (right-left)/2;
        }

        return ans;
    }
}
