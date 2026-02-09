function merge(intervals: number[][]): number[][] {
    if (intervals.length == 0) return []
    intervals = intervals.sort((a,b) => a[0] - b[0])
    
    let answer = []
    let prev = intervals[0]

    for (let i = 1; i < intervals.length; i++) {
        if (prev[1] >= intervals[i][0]) {
            prev[1] = Math.max(prev[1], intervals[i][1])

        } else {
            answer.push(prev)
            prev = intervals[i]
        }
    }

    answer.push(prev)
    return answer
};

merge([[4,7],[1,4]])
merge([[1,3],[2,6],[8,10],[15,18]])