class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res{};
        if (!root) return res;

        queue<Node*> q;
        q.push(root);
        while (!q.empty()){
            int len = q.size();
            vector<int> tmp{};
            for (int i=0; i<len; ++i){
                Node* cur = q.front();
                for (auto& child:cur->children){
                    q.push(child);
                }
                tmp.emplace_back(cur->val);
                q.pop();
            }
            res.emplace_back(tmp);
        } 

        return res;
    }
};