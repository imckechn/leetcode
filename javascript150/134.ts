function canCompleteCircuit(gas: number[], cost: number[]): number {
    let total = 0,
        answer = 0,
        tank = 0;

    for (let idx = 0; idx < gas.length; idx++) {
        const val = gas[idx] - cost[idx];
        total += val;
        tank += val;

        if (total < 0) {
            total = 0;
            answer = idx + 1;
        }
    }
    if (tank < 0) return -1;
    return answer;
}

console.log(canCompleteCircuit([5,8,2,8], [6,5,6,6]))
console.log(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
console.log(canCompleteCircuit([2,3,4], [3,4,3]))