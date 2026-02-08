function isIsomorphic(s: string, t: string): boolean {
    if (s.length != t.length) return false

    let swaps = new Map()
    let used = new Set();

    for (let i = 0; i < s.length; i++) {
        if (swaps.has(s[i]) && swaps.get(s[i]) != t[i]) {
            return false
        
        } else if (!swaps.has(s[i]) && used.has(t[i])) {
            return false
        
        } else if (!swaps.has(s[i])) {
            swaps.set(s[i], t[i])
            used.add(t[i])
        }
    }

    return true;
};

isIsomorphic("egg", "add")