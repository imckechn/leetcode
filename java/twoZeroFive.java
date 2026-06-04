import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) { return false; }

        HashMap<Character, Character> swapped = new HashMap<>();
        HashSet<Character> used = new HashSet<>();

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        for (int i = 0; i < sArr.length; i++ ) {
            if (swapped.containsKey(sArr[i])) {
                if (swapped.get(sArr[i]) != tArr[i]) {
                    return false;
                } else {

                }
            } else {

                if (used.contains(tArr[i])) {
                    return false;
                }
                swapped.put(sArr[i], tArr[i]);
                used.add(tArr[i]);
            }
        }

        return true;
    }
}