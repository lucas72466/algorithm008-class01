class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0;  // 记录重复元素的个数
        for(int i=1;i<nums.size();++i){
            if(nums[i]==nums[i-1]) 
                ++count;
            else
                nums[i-count] = nums[i];
        }

        return nums.size() - count;  
    }


    /*
    另一种写法
    int removeDuplicates(vector<int>& nums) {
       int i = !nums.empty();  // 记录合法索引（应该放到的位置）； 第一个元素肯定不需要移动
       for (auto& n:nums){
           if(n>nums[i-1])
               nums[i++] = n;
       }
       return i;
    }
    */
};