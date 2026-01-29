function hIndex(citations: number[]): number {
    const n: number = citations.length;

    citations.sort((a, b) => a - b);

    for (let i = 0; i < n; i++) {
        if(citations[i] >= n - i) return n - i;
    }

    return 0;
};

console.log(hIndex([3,0,6,1,5]))
console.log(hIndex([0,0]))
console.log(hIndex([0,0,2]))
console.log(hIndex([1,3,1]))