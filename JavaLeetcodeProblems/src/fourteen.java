public class fourteen {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        int index = 0;

        while (true) {
            char letter = 0;
            for (int i = 1; i < strs.length; i ++) {
                if (index < strs[i].length()) {
                    if (letter == 0) {
                        letter = strs[i].charAt(index);
                    } else {

                        if (strs[i].charAt(index) != letter) {
                            return prefix;
                        }

                    }
                } else {
                    return prefix;
                }
            }

            prefix += letter;
        }
    }
}
