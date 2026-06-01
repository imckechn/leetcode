class Solution {
    public boolean isValidSudoku(char[][] board) {

        Set<Character> found = new HashSet<>();
        //Check rows
        for (int i = 0; i < board.length; i++) {
            found.clear();

            for (int j = 0; j < board[i].length; j++) {
                if (found.contains(board[i][j])) {
                    return false;
                } else if (board[i][j] != '.') {
                    found.add(board[i][j]);
                }
            }
        }

        //Check columns
        for (int i = 0; i < board.length; i++) {
            found.clear();

            for (int j = 0; j < board.length; j++) {

                if (found.contains(board[j][i])) {
                    return false;
                } else if (board[j][i] != '.') {
                    found.add(board[j][i]);
                }
            }
        }

        //Check 3x3 squares
        int[][] startingPoints = {
            {0,0},
            {0,3},
            {0,6},
            {3,0},
            {3,3},
            {3,6},
            {6,0},
            {6,3},
            {6,6},
        };

        for (int k = 0; k < startingPoints.length; k++) {
            int x = startingPoints[k][0];
            int y = startingPoints[k][1];

            found.clear();
            for (int i = x; i < x+3; i++) {
                for (int j = y; j < y+3; j++) {
                    if (found.contains(board[i][j])) {
                        return false;
                    } else if (board[i][j] != '.') {
                        found.add(board[i][j]);
                    }
                }
            }
        }

        return true;
    }
}