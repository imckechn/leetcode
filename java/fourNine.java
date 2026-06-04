import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> matches = new HashMap<>();

        for (String str: strs) {
            char[] lst = str.toCharArray();
            Arrays.sort(lst);
            String sorted = new String(lst);

            matches.computeIfAbsent(sorted, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(matches.values());
    }
}