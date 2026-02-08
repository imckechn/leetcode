/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {

    for (let j = 0; j < matrix[0].length/2; j++) {
        for (let i = 0; i < matrix.length; i++) {
            let a = matrix[j][i]
            matrix[j][i] = matrix[matrix[0].length-j-1][i]
            matrix[matrix[0].length-j-1][i] = a
        }
    }

    for (let i = 0; i < matrix.length; i++) {
        for (let j = i; j < matrix[0].length; j++) {
            let a = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = a
        }
    }
};

rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

rotate([[1,2,3],
        [4,5,6],
        [7,8,9]])