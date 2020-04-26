class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res{};
        if (!root) return res;

        stack<Node*> stk;
        stk.push(root);

        while (!stk.empty()){
            root = stk.top();
            stk.pop();
            res.push_back(root->val);
            for (auto it=root->children.rbegin(); it!=root->children.rend(); ++it ){
                stk.push(*it);
            }
        }

        return res;
    }
};

/*
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        _preorder(root, res);
        return res;
    }

    void _preorder(Node* root, vector<int>& vec){
        if (!root) return;
        vec.emplace_back(root->val);
        for (auto& child:root->children){
            _preorder(child,vec);
        }
    }
};
*/