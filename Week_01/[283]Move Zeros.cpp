class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int curPlacement = 0;
		// 将所有非零元素放在数组的前部
        for (int i=0;i<nums.size();++i){
            if(nums.at(i)!=0)
                nums[curPlacement++] = nums.at(i);
        }
		// 将剩余的位置补0
        for (int i=curPlacement;i<nums.size();++i){
            nums[i] = 0;
        }

    }
};

/*
void moveZeroes(vector<int>& nums) {
        // 利用快排的思想, 以0为标定点
        int j = 0;
        for(int i=0;i<nums.size();++i){
            if (nums[i]!=0)
                swap(nums[j++], nums[i]);
        }
    }
*/

/*
void moveZeroes(vector<int>& nums) {
        // 滚雪球， 每次移动最大步数(贪心)
        int snowballSize = 0;
        for (int i=0; i<nums.size(); ++i){
            if (nums[i] != 0)
                swap(nums[i-snowballSize], nums[i]);
            else
                ++ snowballSize;
        }
    }
*/

/*
python巧妙解法：
nums[:] = [x for x in nums if x !=0] + [0] * nums.count(0)
*/