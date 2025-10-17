//import java.util.Dictionary;
//import java.util.Hashtable;
//
//public class Three {
//    public static int lengthOfLongestSubstring(String s) {
//        int maxLength = 0;
//        int currentLength = 0;
//        Dictionary<Character, Integer> dict = new Hashtable<>();
//        for (int i = 0; i < s.length(); i++) {
//            char c = s[i];
//            if (dict.get(c) != null) {
//                if (maxLength < currentLength) {
//                    maxLength = currentLength;
//                }
//
//                int firstIndex = dict.get(c);
//
//                var keys = dict.keys().asIterator();
//
//                var key = keys.next();
//
//                do {
//                    if (dict.get(key) > firstIndex) {
//                        dict.remove(key);
//                    }
//
//                    key = keys.next();
//                } while (key != null);
//
//                currentLength = i - firstIndex + 1;
//
//            } else {
//                dict.put(c, i);
//                currentLength += 1;
//            }
//        }
//    }
//}
