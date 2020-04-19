class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int res = 0;

        while(left<right){
            auto cur = height[left]>height[right]?right:left;
            auto tmp = height[cur]*(right-left);
            res = tmp>res?tmp:res;

            if(height[left]>height[right]) right--;
            else left++;

        }

        return res;
    }
    
};

//缩减搜索空间：https://leetcode-cn.com/problems/container-with-most-water/solution/on-shuang-zhi-zhen-jie-fa-li-jie-zheng-que-xing-tu/