function lengthOfLongestSubstring(s: string): number {
    let letters = new Set<string>
    let answer = 0, pointer = 0

    for (let c of s) {
        if (!letters.has(c)) {
            letters.add(c)
        } else {
            while (s[pointer] != c) {
                letters.delete(s[pointer])
                pointer += 1
            }
            pointer += 1
        }
        answer = Math.max(answer, letters.size)
    }

    return answer
};

console.log(lengthOfLongestSubstring("aabaab!bb"))
console.log(lengthOfLongestSubstring("pwwkew"))