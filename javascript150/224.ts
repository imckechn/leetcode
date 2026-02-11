function calculate(s: string): number {
    let numberSet = new Set([0,1,2,3,4,5,6,7,8,9])
    let answer = 0;
    let nextOperationAddition = true
    for (let i = 0; i < s.length; i++) {
        if (s[i] == '(') {
            let layers = 1
            for (let j = i+1; j < s.length; j++) {
                if (s[j] == '(') {
                    layers += 1
                } else if (s[j] == ')') {
                    layers -= 1

                    if (layers == 0) {
                        let ans = calculate(s.slice(i+1, j))

                        if (nextOperationAddition) {
                            answer += ans
                        } else {
                            answer -= ans
                        }

                        i = j
                        break
                    }
                }
            }
        } else if (s[i] == "+") {
            nextOperationAddition = true
        } else if (s[i] == "-") {
            nextOperationAddition = false
        } else if (s[i] == ' ') {
            continue
        } else if (numberSet.has(+s[i])) {
            let pointer = i
            while (pointer < s.length && numberSet.has(+s[pointer])) {
                pointer++
            }

            let number = s.slice(i, pointer)
            i = pointer-1

            if (nextOperationAddition) {
                answer += +number
            } else {
                answer -= +number
            }
        }
    }
    return answer
};

console.log(calculate("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))")) //23
console.log(calculate(" 2-1 + 2 "))
console.log(calculate("2147483647"))
console.log(calculate("(1+(4+5+2)-3)+(6+8))"))