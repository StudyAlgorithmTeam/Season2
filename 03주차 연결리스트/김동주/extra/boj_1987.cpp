#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

#define MAX_R 20
#define MAX_C 20
#define N_ALPHABETS 26


int R, C;
char grid[MAX_R][MAX_C];
bool visited[N_ALPHABETS];


int backtrack(int r, int c) {
    int ans;
    if (r < 0 || R <= r || c < 0 || C <= c || visited[grid[r][c]]) {
        return 0;
    }
    visited[grid[r][c]] = true;
    ans = backtrack(r-1, c);
    ans = max(ans, backtrack(r, c-1));
    ans = max(ans, backtrack(r+1, c));
    ans = max(ans, backtrack(r, c+1));
    visited[grid[r][c]] = false;
    return ans + 1;
}


void testcase() {
    cin >> R >> C;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cin >> grid[r][c];
            grid[r][c] -= 'A';
        }
    }
    cout << backtrack(0, 0) << endl;
}


int main() {
    int T;

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    testcase();

    return 0;
}