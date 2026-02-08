function wordPattern(pattern: string, s: string): boolean {
    let words = s.split(" ")
    if (words.length != pattern.length) return false;
    
    let match = new Map();
    let alreadyCounted = new Set();
    let i = 0

    for (const c of pattern) {
        if (match.has(c) && match.get(c) != words[i]) {
            return false
        
        }else if (!match.has(c) && alreadyCounted.has(words[i])) {
            return false
        
        } else if (!match.has(c)) {
            match.set(c, words[i])
            alreadyCounted.add(words[i])
        }
        i++
    }

    return true
};

console.log(wordPattern("abba", "dog dog dog dog"))