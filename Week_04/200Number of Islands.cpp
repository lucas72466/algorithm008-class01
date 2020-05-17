class Solution {

private:
    vector<vector<bool>> marked;
    bool inArea(vector<vector<char>>& grid, int x, int y) {
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() || grid[x][y] == '0') return false;
        else return true;
    }
    void bfs(vector<vector<char>>& grid, int x, int y) {
        queue<pair<int, int>> q;
        q.push(pair<int, int>(x, y));

        while (!q.empty()){
            pair<int, int> tmp = q.front();
            q.pop();

            int i = tmp.first , j = tmp.second;
            if (!inArea(grid, i, j)) continue;
            grid[i][j] = '0';
            q.push(pair<int,int>(i - 1, j));
            q.push(pair<int,int>(i + 1, j));
            q.push(pair<int,int>(i , j - 1));
            q.push(pair<int,int>(i , j+1));
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '1') {
                    bfs(grid, i, j);
                    ++count;
                }
            }
        }
        return count;
    }
};