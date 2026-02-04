function strStr(haystack: string, needle: string): number {
    let nextStop: number;
    for (let i = 0; i < haystack.length; i++) {
        if (haystack[i] == needle[0]) {
            let matchFound: Boolean = true;

            for (let j = 1; j < needle.length; j++) {
                if (j+i >= haystack.length) {
                    return -1

                } else if (haystack[i+j] != needle[j]) {
                    matchFound = false
                    break
                }
            }

            if (matchFound) {
                return i
            }
        }
    }

    return -1;
};