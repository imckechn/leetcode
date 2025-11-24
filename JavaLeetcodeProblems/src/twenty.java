import java.util.ArrayList;

public class twenty {
    public boolean isValid(String s) {
        ArrayList<Character> stack = new ArrayList<>();
        char[] str = s.toCharArray();

        for (int i = 0; i < str.length; i++) {
            int maxLen = stack.toArray().length-1;
            if (str[i] == '(' || str[i] == '{' || str[i] == '[') {
                stack.add(str[i]);

            } else if (str[i] == ')') {
                if (stack.get(maxLen) == '(') {
                    stack.remove(maxLen);
                } else {
                    return false;
                }
            } else if (str[i] == ']') {
                if (stack.get(maxLen) == '(') {
                    stack.remove(maxLen);
                } else {
                    return false;
                }
            }else if (str[i] == '}') {
                if (stack.get(maxLen) == '(') {
                    stack.remove(maxLen);
                } else {
                    return false;
                }
            }
        }

        if (stack.toArray().length != 0) {
            return false;
        }
        return true;
    }
}
