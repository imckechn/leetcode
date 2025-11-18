import java.util.HashMap;

public class twelve {
    public String intToRoman(int num) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "I");
        map.put(5, "V");
        map.put(10, "X");
        map.put(50, "L");
        map.put(100, "C");
        map.put(500, "D");
        map.put(1000, "M");

        String answer = "";
        int digit = 1;

        while (num != 0) {
            int rem = num%10;
            if (rem != 0) {
                if (rem == 4) {
                    answer = map.get(5 * digit).concat(answer);
                    answer = map.get(digit).concat(answer);
                    num -= 4;
                } else if (rem == 9) {
                    answer = map.get(10 * digit).concat(answer);
                    answer = map.get(digit).concat(answer);
                    num -= 9;
                } else if (rem == 5) {
                    answer = map.get(5 * digit).concat(answer);
                    num -= 5;
                } else {
                    answer = map.get(digit).concat(answer);
                    num -= 1;
                }

            } else {
                num /= 10;
                digit *= 10;
            }
        }
        return answer;
    }
}
