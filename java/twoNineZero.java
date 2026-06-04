import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");

        if (pattern.length() != words.length) { return false; }

        HashMap<Character, String> elements = new HashMap<>();
        HashSet<String> used = new HashSet<>();

        for (int i = 0; i < words.length; i++) {
            Character key = pattern.charAt(i);
            
            if (elements.containsKey(key)) {
                if (!elements.get(key).equals(words[i])) {
                    return false;
                }
        
            } else if (used.contains(words[i])) {
                return false;

            } else {
                elements.put(key, words[i]);
                used.add(words[i]);
            }
            
        }
        return true;
    }
}