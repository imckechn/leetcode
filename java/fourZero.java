import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class fourZero {
    private List<List<Integer>> comboSum(int[]candidates, int target, ArrayList<Integer> current, int sum, int start) {
        List<List<Integer>> ans = new ArrayList<>();
        
        for (int i = start; i < candidates.length; i++) {
            int candidate = candidates[i];

            if (candidate + sum == target) {
                current.add(candidate);

                ArrayList<Integer> dup = new ArrayList<>(current);

                ans.add(dup);
                current.remove(current.size()-1);
            
            } else if (candidate + sum < target){
                current.add(candidate);
                ans.addAll(comboSum(candidates, target, current, sum+candidate, i+1));
                current.remove(current.size()-1);
            } else {
                break;
            }
        }

        return ans;
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        return comboSum(candidates, target, new ArrayList<>(), 0, 0);
    }
}
