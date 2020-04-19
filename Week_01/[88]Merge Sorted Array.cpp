class Solution {
public:

	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m-1;
        int j = n-1;
        int k = m+n;

        // 从后向前进行合并
        while(i>=0&&j>=0){
            if(nums1[i]>nums2[j])
                nums1[--k] = nums1[i--];
            else
                nums1[--k] = nums2[j--];
        }
        
        // 防止nums2未完全遍历
        while(j>=0)
            nums1[--k] = nums2[j--];
    }
    
};


/*  two-line
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        for (int k=m+n-1,i=m-1,j=n-1;j>=0;--k){
            nums1[k] = i>=0  && nums1[i]>nums2[j] ? nums1[i--]:nums2[j--]; 
        }
    }
*/

