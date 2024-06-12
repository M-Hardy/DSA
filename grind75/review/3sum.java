import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int first = 0; first < nums.length; first++) {

            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }

            int second = first + 1;
            int third = nums.length - 1;

            while (second < third) {

                if (third < nums.length - 1 && nums[third] == nums[third + 1]) {
                    third--;
                    continue;
                }

                int sum = nums[first] + nums[second] + nums[third];

                if (sum == 0) {
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[first]);
                    triplet.add(nums[second]);
                    triplet.add(nums[third]);
                    res.add(triplet);
                    second++;
                    third--;
                }

                else if (sum < 0) {
                    second++;
                }

                else {
                    third--;
                }
            }

        }

        return res;

    }
}