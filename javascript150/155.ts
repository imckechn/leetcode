class MinStack {
    stack: number[];
    minimums: number[];

    constructor() {
        this.stack = []
        this.minimums = []
    }

    push(val: number): void {
        this.stack.push(val)
        if (this.minimums.length == 0 || val <= this.minimums[this.minimums.length-1]) {
            this.minimums.push(val)
        }
    }

    pop(): void {
        let value = this.stack.pop()
        if (value == this.minimums[this.minimums.length-1]) {
            this.minimums.pop()
        }
    }

    top(): number {
        return this.stack[this.stack.length-1]
    }

    getMin(): number {
        return this.minimums[this.minimums.length-1]
    }
}
let min = new MinStack()
min.push(-2)
min.push(0)
min.push(-3)
console.log(min.getMin())
min.pop()
console.log(min.top())
console.log(min.getMin())

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */