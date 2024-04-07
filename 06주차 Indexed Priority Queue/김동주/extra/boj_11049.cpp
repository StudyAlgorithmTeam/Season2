#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <vector>

#define MAX_N 500

using namespace std;


uint32_t N;
uint32_t r[MAX_N];
uint32_t c[MAX_N];
uint32_t memoize[MAX_N][MAX_N];
uint32_t dp(int i, int j);
uint32_t solve(int i, int j);


void testcase() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> r[i] >> c[i];
    }
    cout << dp(0, N-1) << endl;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // int T;
    // cin >> T;
    // while (T--) testcase();

    testcase();

    return 0;
}


uint32_t dp(int i, int j) {
    if (memoize[i][j] == 0) {
        memoize[i][j] = solve(i, j);
    }
    return memoize[i][j];
}


uint32_t solve(int i, int j) {
    if (i == j) {
        return 0;
    }
    if (i+1 == j) {
        return r[i] * c[i] * c[j];
    }

    uint32_t min_ans = -1; // make it underflow
    for (int k = i; k < j; k++) {
        uint32_t ans = dp(i, k) + dp(k+1, j) + r[i]*c[k]*c[j];
        if (min_ans > ans) {
            min_ans = ans;
        }
    }

    return min_ans;
}