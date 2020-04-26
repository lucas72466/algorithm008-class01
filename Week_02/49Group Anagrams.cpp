class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, int> map;
        int index = 0;

        for (string str:strs){
            auto tmp = str;

            sort(tmp.begin(), tmp.end());
            if (map.count(tmp)){
                res[map[tmp]].push_back(str);
            }
            else{
                res.push_back(vector<string> {str});
                map[tmp] = index++;
            }
        }

        return res;

    }
};