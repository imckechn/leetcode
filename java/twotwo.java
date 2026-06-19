class Solution {
    private List<String> open(int O, int C, StringBuilder currString) {
        currString.append('(');
        O -= 1;
        int strLen = currString.length(); 

        List<String> answer = new ArrayList<>();

        if (O > 0) {
            answer.addAll(this.open(O, C, currString));
            currString.setLength(strLen);
        }

        answer.addAll(this.close(O, C, currString));
        return answer;
    }

    private List<String> close(int O, int C, StringBuilder currString) {
        if (C == 0) {
            return List.of(currString.toString());
        }

        int strLen = currString.length();
        List<String> answer = new ArrayList<>();

        if (C > O) {  
            currString.append(')');
            answer.addAll(this.close(O, C - 1, currString));  
        }

        if (O > 0) {
            answer.addAll(this.open(O, C, currString));
            currString.setLength(strLen);
        }

        currString.setLength(strLen);
        return answer;
    }

    public List<String> generateParenthesis(int n) {
        return this.open(n, n, new StringBuilder());
    }
}