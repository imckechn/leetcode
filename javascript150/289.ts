/**
 Do not return anything, modify board in-place instead.
 */
function messAround(board: number[][], i: number, j: number): number {
    let sum = 0

    //Top row
    if (board.length >= 1 && board[i].length >= 1 && i >= 1 && j >= 1) {
        if (board[i-1][j-1] == 1) {
            sum+=1
        }
    }

    if (board.length >= 1 && i >= 1) {
        if (board[i-1][j] == 1) {
            sum+=1
        }
    }

    if (board.length >= 1 && i >= 1 && j < board[i].length - 1) {
        if (board[i-1][j+1] == 1) {
            sum+=1
        }
    }

    //Left and right
    if (board[i].length >= 1 && j >= 1) {
        if (board[i][j-1] == 1) {
            sum+=1
        }
    }

    if (j < board[i].length - 1) {
        if (board[i][j+1] == 1) {
            sum+=1
        }
    }

    //Bottom row
    if (board[i].length >= 1 && i < board.length-1 && j >= 1) {
        if (board[i+1][j-1] == 1) {
            sum+=1
        }
    }

    if (board.length >= 1 && i < board.length-1) {
        if (board[i+1][j] == 1) {
            sum+=1
        }
    }

    if (board.length >= 1 && i < board.length-1 && j < board[i].length - 1) {
        if (board[i+1][j+1] == 1) {
            sum+=1
        }
    }

    return sum
}

function gameOfLife(board: number[][]): void {
    let swaps: number[][] = []

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            let total = messAround(board, i, j)

            if (board[i][j] == 1) {
                if (total < 2 || total > 3) {
                    swaps.push([i,j])
                }
            } else {
                if (total == 3) {
                    swaps.push([i,j])
                }
            }
        }
    }

    for (const swap of swaps) {
        if (board[swap[0]][swap[1]] == 1) {
            board[swap[0]][swap[1]] = 0
        } else {
            board[swap[0]][swap[1]] = 1
        }
    }
};