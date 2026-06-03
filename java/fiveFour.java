class Solution {
    public List<Integer> goRight(int[][] matrix, int[] currentPos, List<Integer> visited) {
        int x = currentPos.get(0);
        int y = currentPos.get(1);

        while (x < matrix.length-1) {
            x += 1;

            if (visited.contains(matrix[x][y])) {
                x -= 1;
                break;
            
            } else {
                visited.add(matrix[x][y]);
            }
        }

        return List.of(x,y);
    }

    public List<Integer> goDown(int[][] matrix, List<Integer> currentPos, List<Integer> visited) {
        int x = currentPos.get(0);
        int y = currentPos.get(1);

        while (y < matrix[x].length-1) {
            y += 1;

            if (visited.contains(matrix[x][y])) {
                y -= 1;
                break;
            
            } else {
                visited.add(matrix[x][y]);
            }
        }

        return List.of(x,y);
    }


    public List<Integer> goLeft(int[][] matrix, List<Integer> currentPos, List<Integer> visited) {
        int x = currentPos.get(0);
        int y = currentPos.get(1);

        while (x > 0) {
            x -= 1;

            if (visited.contains(matrix[x][y])) {
                x += 1;
                break;
            
            } else {
                visited.add(matrix[x][y]);
            }
        }

        return List.of(x,y);
    }

    public List<Integer> goUp(int[][] matrix, List<Integer> currentPos, List<Integer> visited) {
        int x = currentPos.get(0);
        int y = currentPos.get(1);

        while (y > 0) {
            y -= 1;

            if (visited.contains(matrix[x][y])) {
                y += 1;
                break;
            
            } else {
                visited.add(matrix[x][y]);
            }
        }

        return List.of(x,y);
    }

    public List<Integer> spiralOrder(int[][] matrix) {
        List[] visited = new List[matrix.length * matrix[0].length];
        int[] currentPosition = {0, 0};

        while (true) {
            currentPosition = goRight(matrix, currentPosition, visited);
            if (currentPosition[0] == -1) { return visited; }

            currentPosition = goDown(matrix, currentPosition, visited);
            if (currentPosition[0] == -1) { return visited; }

            currentPosition = goLeft(matrix, currentPosition, visited);
            if (currentPosition[0] == -1) { return visited; }

            currentPosition = goRight(matrix, currentPosition, visited);
            if (currentPosition[0] == -1) { return visited; }
        }
    }
}