class Solution {
    public int lengthOfLastWord(String s) {
        String[] words = s.split("\\s+");
        String finalWord = words[words.length-1];
        return finalWord.length();
    }
}