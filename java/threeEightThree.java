class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> letters = new HashMap<>();

        char[] randomNoteArr = ransomNote.toCharArray();
        char[] magazineArr = magazine.toCharArray();

        for (char c: magazineArr) {
            letters.put(c, letters.getOrDefault(c, 0) + 1);
        }

        for (char c: randomNoteArr) {
            letters.put(c, letters.getOrDefault(c, 0) - 1);
        }

        for (char c: letters.keySet()) {
            if (letters.get(c) < 0) {
                return false;
            }
        }

        return true;
    }
}