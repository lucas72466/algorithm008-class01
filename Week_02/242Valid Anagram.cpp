class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;

        int counter[26] = {0};

        for (int i=0; i<s.size(); ++i){
            ++ counter[s[i]-'a'];
            -- counter[t[i]-'a'];
        }

        for (int& i:counter){
            if (i) return false;
        }


        return true;
    }
};


/*

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        distinct = set(s) 

        for i in distinct:
            if s.count(i) != t.count(i): 
                return False

        return True
*/