import java.util.ArrayList;
import java.util.List;

public class sevenTeen {
    public List<String> letterCombinations(String digits) {
        List<String> answer = new ArrayList<>();

        char[][] phoneNumbers = {
                {},
                {},
                {'a', 'b', 'c'},
                {'d', 'e', 'f'},
                {'g', 'h', 'i'},
                {'j', 'k', 'l'},
                {'m', 'n', 'o'},
                {'p', 'q', 'r', 's'},
                {'t', 'u', 'v'},
                {'w', 'x', 'y', 'z'}
        };
        char[] list = digits.toCharArray();

        for (int i = 0; i < list.length; i++) {
            List<String> copy = answer;

            for (int j = 0; j < char[])
        }
    }

}
