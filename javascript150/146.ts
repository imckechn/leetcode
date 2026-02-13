class DoublelyListNode {
    key: number
    val: number
    newer: DoublelyListNode | null
    older: DoublelyListNode | null
    constructor(key: number, val: number, newer?: DoublelyListNode | null, older?: DoublelyListNode | null) {
        this.key = key
        this.val = val
        this.newer = (newer===undefined ? null : newer)
        this.older = (older===undefined ? null : older)
    }
}

class LRUCache {
    mostRecent: Map<number, DoublelyListNode>;
    oldest: DoublelyListNode | null;
    newest: DoublelyListNode | null;
    maxCapacity: number;
    currentCapacity: number;

    constructor(capacity: number) {
        this.mostRecent = new Map()
        this.oldest = null
        this.newest = null
        this.maxCapacity = capacity
        this.currentCapacity = 0;
    }

    get(key: number): number {
        if (this.mostRecent.has(key)) {
            let elem = this.mostRecent.get(key)

            if (elem?.older) {
                elem.older.newer = elem.newer
            }

            if (elem?.newer) {
                elem.newer.older = elem.older
            }

            elem!.older = this.newest
            elem!.newer = null
            this.newest!.newer = elem! 
            this.newest = elem!

            if (this.oldest == this.newest && this.currentCapacity > 1) {
                this.oldest = this.oldest.older
            }

            return this.newest!.val

        } else {
            return -1;
        }
    }

    put(key: number, value: number): void {
        if (this.mostRecent.has(key)) {
            this.mostRecent.get(key)!.val = value
        
        } else if (this.currentCapacity < this.maxCapacity) { //Add a new one
            this.currentCapacity++

            if (!this.newest) {
                this.newest =  new DoublelyListNode(key, value, null, null)
                this.oldest = this.newest

                this.mostRecent.set(key, this.newest)

            } else {
                let newHead = new DoublelyListNode(key, value, null, this.newest)
                this.newest.newer = newHead
                this.newest = this.newest.newer

                this.mostRecent.set(key, newHead)
            }
        } else {
            let toBeDeleted = this.oldest
            this.oldest = this.oldest!.newer
            this.oldest!.older = null

            this.mostRecent.delete(toBeDeleted!.key)

            let newHead = new DoublelyListNode(key, value, null, this.newest)
            this.newest!.newer = newHead
            this.newest = this.newest!.newer

            this.mostRecent.set(key, newHead)
        }
    }
}


let cache = new LRUCache(1)
cache.put(2,1)
console.log(cache.get(1))



cache.put(1,1)
cache.put(2,2)
console.log(cache.get(1))
cache.put(3,3)
console.log(cache.get(2))
cache.put(4,4)
console.log(cache.get(1))
console.log(cache.get(3))
console.log(cache.get(4))


/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */