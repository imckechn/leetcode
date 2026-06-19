public class eleven {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int largest = 0;

        while (left < right) {
            int volume = Math.min(height[left], height[right]) * (right - left);
            largest = Math.max(largest, volume);

            if (height[left] < height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return largest;
    }
}
