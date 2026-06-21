import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class threeNine {
    HashSet<List<Integer>> comboSum(int[] candidates, int target, ArrayList<Integer> current, int sum) {

        HashSet<List<Integer>> ans = new HashSet<>();

        for (int candidate: candidates) {
            if (sum+candidate == target) {
                current.add(candidate);
                ArrayList<Integer> valToBeAdded = new ArrayList<>(current);
                valToBeAdded.sort(null);
                ans.add(valToBeAdded);
                current.remove(current.size()-1);

            }  else if (sum+candidate < target) {
                current.add(candidate);
                ans.addAll(comboSum(candidates, target, current, sum+candidate));
                current.remove(current.size()-1);
            }
        }

        return ans;
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        HashSet<List<Integer>> hashAns = comboSum(candidates, target, new ArrayList<>(), 0);
        List<List<Integer>> ans = new ArrayList<>();

        for (List<Integer> elem: hashAns) {
            ans.add(elem);
        }
        return ans;        
    }
}
