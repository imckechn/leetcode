import java.util.HashMap;
import java.util.Map;

public class thirteen {
    public int romanToInt(String s) {
        int answer = 0;
        Map<Character, Integer> letters = new HashMap<>();
        letters.put('I', 1);
        letters.put('V', 5);
        letters.put('X', 10);
        letters.put('L', 50);
        letters.put('C', 100);
        letters.put('D', 500);
        letters.put('M', 1000);

        char[] numerals = s.toCharArray();

        for (int i = 0; i < numerals.length; i++) {
            if (i != numerals.length-1 && letters.get(numerals[i]) < letters.get(numerals[i+1])) {
                if (numerals[i] == 'C' && numerals[i+1] == 'M') {
                    answer += 900;

                } else if (numerals[i] == 'C' && numerals[i+1] == 'D') {
                    answer += 400;

                } else if (numerals[i] == 'X' && numerals[i+1] == 'C') {
                    answer += 90;

                } else if (numerals[i] == 'X' && numerals[i+1] == 'L') {
                    answer += 40;

                }else if (numerals[i] == 'I' && numerals[i+1] == 'X') {
                    answer += 9;

                } else if (numerals[i] == 'I' && numerals[i+1] == 'V') {
                    answer += 4;
                }
                i+=1;

            } else {
                answer += letters.get(numerals[i]);
            }
        }

        return answer;
    }
}
