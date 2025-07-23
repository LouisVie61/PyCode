// Yêu cầu:
// Viết chương trình tìm đường ra khỏi mê cung kích thước n×m. Biết ta chỉ có thế đi ngang hoặc dọc trong mê cung và không đi lại các ô đã đi qua.
// Input:
// Dòng đầu tiên chứa 2 số nguyên dương n và m là số hàng và số cột của mê cung n dòng tiếp theo mỗi dòng chứa m số 0 hoặc 1. Nếu giá trị của một ô là 0 ô đó có thể đi qua, nếu là 1 ô đó không thể đi qua
// Output:
// Tìm đường đi từ góc trái trên xuống góc phải dưới, in ra màn hình mê cung với các ô trong đường đi được đánh số 2.

#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<vector<int>> grid;
vector<vector<bool>> visited;

// up, right, down, left
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

bool isValid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m &&
        grid[x][y] == 0 && visited[x][y] == false;
}

bool dfs(int x, int y) {
    if (x == n-1 && y == m-1) {
        grid[x][y] = 2;
        return true;
    }
    
    grid[x][y] = 2;
    visited[x][y] = true;
    
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir], ny = y + dy[dir];
        
        if (isValid(nx, ny)) {
            if (dfs(nx, ny)) return true;
        }
    }
    
    grid[x][y] = 0;
    visited[x][y] = false;
    return false;
}


int main() {
    cin >> n >> m;
    
    grid.resize(n, vector<int>(m));
    visited.resize(n, vector<bool>(m, false));
    
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> grid[i][j];

    if (dfs(0, 0)) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                cout << grid[i][j] << " ";
            cout << endl;
        }
    } else {
        cout << "No direction" << endl;
    }

    return 0;
}