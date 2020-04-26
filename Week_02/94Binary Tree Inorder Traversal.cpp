class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res{};
        if (!root) return res;

        stack<TreeNode*> stk;
        while (root || !stk.empty()){
            while (root){ // 不断向左子树的方向直到最左的叶子节点，并且把途径的节点压栈 （模拟递归调用）
                stk.push(root);
                root = root->left;
            }  
            // 如果当前节点为空， 说明已经到达左尽头， 从栈中弹出节点并加入数组 ，然后转向右节点
            root = stk.top();
            stk.pop();
            res.push_back(root->val);
            root = root->right;
        }

        return res;
    }
};