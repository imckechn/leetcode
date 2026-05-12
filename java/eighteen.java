class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            int maxSize = Math.min(prefix.length(), strs[i].length());
            for (int j = 0; j < maxSize; j++) {
                if (prefix.charAt(j) != strs[i].charAt(j)) {
                    prefix = prefix.substring(0, j);
                    break;
                }
            }

            if (prefix.length() > maxSize) {
                prefix = prefix.substring(0, maxSize);
            }
        }

        return prefix;
    }
}