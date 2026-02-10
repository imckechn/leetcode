function insert(intervals: number[][], newInterval: number[]): number[][] {
    let i = 0
    let inserted = false;
    for (i = 0; i < intervals.length; i++) {
        if (newInterval[0] <= intervals[i][1] && newInterval[1] >= intervals[i][0]) {
            inserted = true
            intervals[i][0] = Math.min(intervals[i][0], newInterval[0])
            intervals[i][1] = Math.max(intervals[i][1], newInterval[1])
            break
        }
    }

    if (!inserted) {
        intervals.push(newInterval)
    }

    intervals = intervals.sort((a,b) => a[0]-b[0])

    for (let j = i+1; j < intervals.length; j++) {
        if (intervals[i][1] < intervals[j][0]) {
            break
        
        } else if (intervals[i][1] >= intervals[j][1]) {
            intervals.splice(j, 1)
            j--

        } else if (intervals[i][1] >= intervals[j][0]) {
            intervals[i][1] = intervals[j][1];
            intervals.splice(j, 1)
            j--
        } else {
            break
        }
    }

    return intervals
};

console.log(insert([[1,5]], [0,1]))
console.log(insert([[1,5]], [0, 0]))
