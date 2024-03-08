#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

#define MOD (1000000007)
#define MAX_N (50000)
#define MAX_M (200000)

using namespace std;


long long madd(long long a, long long b, long long mod) {
    return ((a % mod) + (b % mod)) % mod;
}

long long mmul(long long a, long long b, long long mod) {
    return ((a % mod) * (b % mod)) % mod;
}

struct edge {
    int index;
    int diff;
};


bool cmp_edges(const struct edge &p1, const struct edge &p2) {
    return p1.index < p2.index;
}


long long FACTORIAL[MAX_M+1];

int n;
int m;
int A[MAX_N+1];
struct edge edges[2*(MAX_M+1)];
long long frequency[MAX_M+1];


void testcase() {
    cin >> n >> m;

    // O(n)
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // O(m)
    int n_edges = 0;
    for (int j = 0; j < m; j++) {
        int x, y;

        cin >> x;
        edges[n_edges].index = x;
        edges[n_edges].diff = 1;
        n_edges++;

        cin >> y;
        edges[n_edges].index = y+1;
        edges[n_edges].diff = -1;
        n_edges++;
    }


    // O(n log n + m log m)
    sort(A, A+n);
    sort(edges, edges+n_edges, cmp_edges);

    // O(m)
    memset(frequency, 0, sizeof(frequency));

    // O(m)
    int last_index = 1;
    int last_n_ranges = 0;
    for (int i = 0; i < n_edges; i++) {
        frequency[last_n_ranges] += (edges[i].index - last_index);
        last_n_ranges += edges[i].diff;
        last_index = edges[i].index;
    }
    frequency[0] += (n + 1 - last_index);

    // O(n+m)
    long long max_s = 0;
    long long n_cases = 1;
    int index = n-1;
    for (int n_ranges = m; n_ranges >= 0; n_ranges--) {
        // n_ranges개의 구간에 포함된 원소가 n_elements개.
        int n_elements = frequency[n_ranges];
        for (int i = 0; i < n_elements; i++) {
            max_s += n_ranges * A[index--];
        }
        n_cases = mmul(n_cases, FACTORIAL[n_elements], MOD);
    }

    cout << max_s << ' ' << n_cases << endl;
}

void init() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 팩토리얼을 미리 구해놓는다.
    FACTORIAL[0] = 1;
    for (long long i = 1; i <= MAX_M; i++) {
        FACTORIAL[i] = mmul(FACTORIAL[i-1], i, MOD);
    }
}

int main() {
    int T;
    init();
    for (cin >> T; T; T--) testcase();
    return 0;
}