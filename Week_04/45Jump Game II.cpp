class Solution {
public:
    int jump(vector<int>& nums) {
        int res = 0;
        int start = 0;
        int end = 0;

        while (end<nums.size()-1){
            int maxPos = 0;
            for (int i=start; i<=end; ++i)
                maxPos = max(maxPos, i+nums[i]);
            start = end+1;
            end = maxPos;
            ++res;
        }

        return res;
    }
};