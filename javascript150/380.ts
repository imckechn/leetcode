class RandomizedSet {
    dictionary: Map<number, number>;

    constructor() {
        this.dictionary = new Map();
    }

    insert(val: number): boolean {
        if (this.dictionary.has(val)) {
            return false;

        } else {
            this.dictionary.set(val, this.dictionary.size)
            return true;
        }
    }

    remove(val: number): boolean {
        if (this.dictionary.has(val)) {
            this.dictionary.delete(val)
            return true
        }
        return false
    }

    getRandom(): number {
        let arr: number[] = [];
        let keys = this.dictionary.keys();

        for (const val of keys) {
            arr.push(val);
        }
        return arr[Math.floor(Math.random() * arr.length)];
    }
}

let rand = new RandomizedSet()
console.log(rand.insert(1))
console.log(rand.remove(2))
console.log(rand.insert(2))
console.log(rand.getRandom())
console.log(rand.remove(1))
console.log(rand.insert(2))
console.log(rand.getRandom())

