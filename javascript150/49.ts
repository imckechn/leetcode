function groupAnagrams(strs: string[]): string[][] {
    let matches = new Map()

    for (const str of strs) {
        let copy = str.split('').sort().join()

        if (!matches.has(copy)) {
            matches.set(copy, [str])
        } else {
            let elem = matches.get(copy)
            elem.push(str)
            matches.set(copy, elem)
        }
    }

    let answer = []
    for (const key of matches.keys()) {
        answer.push(matches.get(key))
    }
    return answer
};

groupAnagrams(["eat","tea","tan","ate","nat","bat"])