import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) { return false; }

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        HashMap<Character, Integer> swaps = new HashMap<>();

        for (char c: sArr) {
            swaps.put(c, swaps.getOrDefault(c, 0) + 1);
        }

        for (char c: tArr) {
            swaps.put(c, swaps.getOrDefault(c, 0) - 1);
        }

        for (char c: swaps.keySet()) {
            if (swaps.get(c) < 0) {
                return false;
            }
        }

        return true;
    }
}