public class nine {
    public boolean isPalindrome(int x) {
//        if (x < 0) {
//            return false;
//        }
//
//        char[] number = String.valueOf(x).toCharArray();
//        if (number.length == 1) {
//            return true;
//        }
//
//        int left = number.length/2;
//        int right = 0;
//        if (number.length%2 == 0) {
//            right = left;
//            left -= 1;
//        } else {
//            right = left + 1;
//            left -= 1;
//        }
//
//        while (left >= 0) {
//            if (number[left] != number[right]) {
//                return false;
//            }
//            left -= 1;
//            right += 1;
//        }
//
//        return true;


        if (x < 0) {
            return false;
        }

        char[] number = String.valueOf(x).toCharArray();

        int left = 0;
        int right = number.length -1;

        while (left < right) {
            if (number[left] != number[right]) {
                return false;
            }

            left += 1;
            right -= 1;
        }

        return true;
    }
}
