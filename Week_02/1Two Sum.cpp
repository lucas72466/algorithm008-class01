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

/*

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        table = {}
        index = 0 
        res = []
        for num in nums:
            if target-num in table:
                res.append(table[target-num])
                res.append(index)
                return res
            table[num] = index
            index += 1

        return [-1]*2

*/