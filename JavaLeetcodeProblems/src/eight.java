import java.util.HashMap;
import java.util.Map;
import java.util.Objects;


public class eight {
    public int myAtoi(String s) {
        long answer = 0;
        String[] characters = s.split("");
        boolean firstCharacterZero = true;
        boolean encounterdANumber = false;
        long sign = 1;
        boolean signEncountered = false;

        Map<String, Integer> map = new HashMap<>();
        map.put("0", 0);
        map.put("1", 1);
        map.put("2", 2);
        map.put("3", 3);
        map.put("4", 4);
        map.put("5", 5);
        map.put("6", 6);
        map.put("7", 7);
        map.put("8", 8);
        map.put("9", 9);

        for (int i = 0; i < s.length(); i++) {
            String c = characters[i];
            if (answer >= Integer.MAX_VALUE || answer <= Integer.MIN_VALUE) {
                break;
            }

            if (!map.containsKey(c)) {
                if (!encounterdANumber && Objects.equals(c, " ") && !signEncountered) {
                    continue;
                } else if (!encounterdANumber && Objects.equals(c, "+") && !signEncountered) {
                    signEncountered = true;

                } else if (!encounterdANumber && Objects.equals(c, "-") && !signEncountered) {
                    signEncountered = true;
                    sign = -1;
                } else {
                    break;
                }
            } else { //It's a number
                encounterdANumber = true;
                if (!Objects.equals(c, "0")) {
                    answer *= 10;
                    answer += map.get(c);
                    firstCharacterZero = false;
                } else {
                    if (!firstCharacterZero) {
                        answer *= 10;
                        answer += map.get(c);
                    }
                }
            }
        }
        answer *= sign;
        if (answer > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        if (answer < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        return (int) Math.floor(answer);
    }
}
