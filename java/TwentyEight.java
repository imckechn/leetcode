class Solution {
    public int strStr(String haystack, String needle) {
        
        for (int i = 0; i < haystack.length(); i++) {
            int matchFound = 0;
            for (int j = 0; j < needle.length(); j++) {
                if (haystack.length() <= i+j || haystack.charAt(i+j) != needle.charAt(j)) {
                    matchFound = 1;
                    break;
                }
            }

            if (matchFound == 0) {
                return i;
            }
        }
        return -1;
    }
}