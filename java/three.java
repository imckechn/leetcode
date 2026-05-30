class Solution {
    public int lengthOfLongestSubstring(String s) {

        Set<Character> found = new HashSet();
        int left = 0;
        int right = -1;
        int maxSize = 0;

        char[] charArr = s.toCharArray();

        while (right < charArr.length-1) {
            right += 1;

            if ( found.contains(charArr[right])) {
                
                while (charArr[left] != charArr[right]) {
                    found.remove(charArr[left]);
                    left += 1;
                }
                found.remove(charArr[left]);
                left += 1;
            }

            found.add(charArr[right]);
            
            if (found.size() > maxSize) {
                maxSize = found.size();
            }
        }

        return maxSize;
    }
}