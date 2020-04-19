class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i=digits.size()-1; i>=0; --i){
            if(digits[i]<9){
                ++ digits[i];
                return digits;
            }
            else
                digits[i] = 0;
        }

        digits[0] = 1;
        digits.push_back(0);  // 避免整个数组的拷贝， 从尾部推入0

        return digits;
    }
};

/*
    vector<int> plusOne(vector<int>& digits) {
        bool carry = 1;
        for (int i=digits.size()-1; i>=0 && carry; --i){
            carry = (++digits[i]%=10) == 0;
        }

        if(carry){
            digits[0] = 1;
            digits.push_back(0);
        }

        return digits;
    }

*/

/*
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)

*/