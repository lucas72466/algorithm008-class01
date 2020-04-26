class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {

        vector<int> res{};
        if (root==NULL) return res;
        
        stack<TreeNode*> stk;
        stk.push(root);
        while (!stk.empty()){
            root = stk.top();
            res.push_back(root->val);
            stk.pop();
            if (root->right) stk.push(root->right); // 注意压栈顺序，因为是后入先出，所以说先压入右节点
            if (root->left) stk.push(root->left);
        }

        return res;
    }
};