#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

#define INF 1000000
#define MAX_N 100

using namespace std;

typedef long long int64;


int N, M;

int64 m[MAX_N+1];
int64 c[MAX_N+1];


int64 dp(int index, int64 memory) {
    if (memory >= M) return 0;
    if (index >= N) return INF;
    return min(
        dp(index+1, memory+m[index]) + c[index],
        dp(index+1, memory)
    );
}


void testcase() {
    int i;
    cin >> N >> M;
    for (i = 0; i < N; i++) cin >> m[i];
    for (i = 0; i < N; i++) cin >> c[i];
    cout << dp(0, 0) << endl;
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