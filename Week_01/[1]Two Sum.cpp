class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int,int> hash;
        for(int i=0;i<nums.size();++i){
            if(hash.find(target-nums[i])==hash.end())
                hash[nums[i]] = i;
            else
                return vector<int>{hash[target-nums[i]], i};
        }

        return vector<int>{};
    }
};

// 1.暴力法，对每个num都搜索一遍数组
// 2.在暴力法的基础上缩减搜索空间, 只对其后的数组进行遍历
// 3.用哈希表进行存储， 加快访问