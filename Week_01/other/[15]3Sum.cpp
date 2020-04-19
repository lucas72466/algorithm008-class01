class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> res;

        if(nums.size()<3)
            return res;
        
        // 双指针基础：数组是有序的
        std::sort(nums.begin(), nums.end());
        
        for(int i=0;i<nums.size()-2;){

            auto target = -nums[i];

            if(target<0)
                break;

            int l = i+1;
            int r = nums.size() -1 ;
            
            while(l<r){
                auto sum = nums[l]+nums[r];

                if(sum<target)
                    while(l<r&&nums[l]==nums[++l]);
                else if(sum>target)
                    while(l<r&&nums[r]==nums[--r]);
                else{
                    res.push_back(std::vector<int>{nums[i],nums[l],nums[r]});
                    while(l<r&&nums[l]==nums[++l]);
                    while(l<r&&nums[r]==nums[--r]);
                }

            }

            while(++i<nums.size()&&nums[i]==nums[i-1]);

        }

        return res;

    }


};