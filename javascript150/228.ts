function summaryRanges(nums: number[]): string[] {
    if (nums.length == 0) return []

    let answer: string[] = []
    let start = nums[0]
    let prev = nums[0]

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] != prev+1) {
            if (start == prev) {
                answer.push(start + "")
            
            } else {
                answer.push(start + "->" + prev)
            }

            start = nums[i]
        }
        prev = nums[i]
    }

    if (start == prev) {
        answer.push(start.toString())
    
    } else {
        answer.push(start + "->" + prev)
    }

    return answer
};