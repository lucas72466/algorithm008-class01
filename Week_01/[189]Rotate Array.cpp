class Solution {
public:
    void rotate(vector<int>& nums, int k) {

        int len = nums.size();
        k %= len;  // 使其落在数组长度的范围内
        if (k!=0)
            //反转整个数组
            reverse(nums, 0,len-1);
            //对前k%len个元素进行反转
            reverse(nums, 0,k-1);
            //对剩余元素进行反转
            reverse(nums, k,len-1);
    }

    // 对l...r这段闭区间内的元素进行反转
    void reverse(vector<int>& nums,int l, int r){
        while (l<r){
            int tmp = nums[l];
            nums[l++] = nums[r];
            nums[r--] = tmp;
        }
    }
  
};

/*  python solution 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:]+nums[:-k]
*/