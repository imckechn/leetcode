function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length) return false;

    let countA = new Map()
    let countB = new Map()

    for (const c of s) {
        if (!countA.has(c)) {
            countA.set(c, 1)
        } else {
            countA.set(c, countA.get(c) + 1)
        }
    }

    for (const c of t) {
        if (!countB.has(c)) {
            countB.set(c, 1)
        } else {
            countB.set(c, countB.get(c) + 1)
        }
    }

    for (const key of countA.keys()) {
        if (countA.get(key) != countB.get(key)) return false
    }
    return true
};

console.log(isAnagram("cat", "rat"))