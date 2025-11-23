public class six {
    public String convert(String s, int numRows) {
        char[] str = s.toCharArray();
        char[][] zigzag = createZigZag(str, numRows);

        String answer = "";
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < str.length; j++) {
                if (zigzag[i][j] == '\u0000') {
                    break;
                }
                if (zigzag[i][j] != ' '){
                    answer = answer.concat(String.valueOf(zigzag[i][j]));
                }
            }
        }

        return answer;
    }

    public char[][] createZigZag(char[] s, int numRows) {
        char[][] arr = new char[numRows][s.length];
        int row = 0;
        int charCounter = 0;
        int counter = 0;

        while (charCounter != s.length) {
            if (counter >= numRows-1) {
                counter = 0;
            }

            //Vertical Line
            if (counter == 0) {
                for (int j = 0; j < numRows; j++) {
                    arr[j][row] = s[charCounter];
                    charCounter += 1;

                    if (charCounter == s.length) {
                        break;
                    }
                }

                //Diagonal element
            } else {
                for (int j = 0; j < numRows; j++) {
                    if (j == numRows - counter - 1) {
                        arr[j][row] = s[charCounter];
                        charCounter += 1;
                    } else {
                        arr[j][row] = ' ';
                    }
                }
            }

            row += 1;
            counter += 1;
        }

        return arr;
    }
}
