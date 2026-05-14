import java.util.Enumeration;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> dict = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (dict.containsKey(nums[i])) {
                dict.put( nums[i], dict.get(nums[i]) + 1 );
            } else {    
                 dict.put( nums[i], 1 );
            }
        }

        int largest = Integer.MIN_VALUE;
        int largestKey = 0;

        for (Integer key : dict.keySet()) {

            if (dict.get(key) > largest) {
                largest = Math.max(largest, dict.get(key));
                largestKey = key;
            }
        }

        return largestKey;
    }
}