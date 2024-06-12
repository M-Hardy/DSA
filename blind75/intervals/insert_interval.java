import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();

        for (int[] itv : intervals) {
            if (newInterval == null || itv[1] < newInterval[0]) {
                res.add(itv);
            } else if (itv[0] > newInterval[1]) {
                res.add(newInterval);
                res.add(itv);
                newInterval = null;
            } else {
                newInterval[0] = Math.min(itv[0], newInterval[0]);
                newInterval[1] = Math.max(itv[1], newInterval[1]);
            }
        }

        if (newInterval != null) {
            res.add(newInterval);
        }

        return res.toArray(new int[res.size()][]);
    }
}