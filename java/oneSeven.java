import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class oneSeven {
    public List<String> letterCombinations(String digits) {
        HashMap<Character, List<String>> phone = new HashMap<>();
        phone.put('2', List.of("a", "b", "c"));
        phone.put('3', List.of("d", "e", "f"));
        phone.put('4', List.of("g", "h", "i"));
        phone.put('5', List.of("j", "k", "l"));
        phone.put('6', List.of("m", "n", "o"));
        phone.put('7', List.of("p", "q", "r", "s"));
        phone.put('8', List.of("t", "u", "v"));
        phone.put('9', List.of("w", "x", "y", "z"));

        List<String> answer = new ArrayList<>();
        
        for (char num: digits.toCharArray()) {
            if (answer.size() == 0) {
                answer.addAll(phone.get(num));
            
            } else {
                List<String> newAns = new ArrayList<>();

                for (String elem: phone.get(num)) {
                    for (String answerElem: answer) {
                        newAns.add(answerElem + elem);
                    }
                }

                answer = newAns;
            } 
        }

        return answer;
    }
}
