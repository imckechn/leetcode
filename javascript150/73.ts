/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    let columns = new Set<number>
    let rows = new Set<number>

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] == 0) {
                rows.add(i)
                columns.add(j)
            } 
        }
    }

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (rows.has(i) || columns.has(j)) {
                matrix[i][j] = 0
            } 
        }
    }
};

setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])