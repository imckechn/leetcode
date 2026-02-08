function isIsomorphic(s: string, t: string): boolean {
    if (s.length != t.length) {
        return false
    }

    let countA = new Map()
    let countB = new Map()

    for (const c of s) {
        const currentCount = countA.get(c) || 0;
        countA.set(c, currentCount + 1);
    }

    for (const c of t) {
        const currentCount = countB.get(c) || 0;
        countB.set(c, currentCount + 1);
    }

    let valuesA = [...countA.values()].sort((a,b) => a-b)
    let valuesB = [...countB.values()].sort((a,b) => a-b)

    for (let i = 0; i < valuesA.length; i++) {
        if (valuesA[i] != valuesB[i]) return false
    }
    return true
};

isIsomorphic("egg", "add")