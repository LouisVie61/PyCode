#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

long long gcd_ll(long long a, long long b) {
    return b == 0 ? a : gcd_ll(b, a % b);
}

long long lcm_ll(long long a, long long b) {
    return a / gcd_ll(a, b) * b;
}

long long findLCM(const vector<int>& A) {
    long long res = A[0];
    for (int i = 1; i < (int)A.size(); i++)
        res = lcm_ll(res, A[i]);
    return res;
}

long long findGCD(const vector<int>& B) {
    long long res = B[0];
    for (int i = 1; i < (int)B.size(); i++)
        res = gcd_ll(res, B[i]);
    return res;
}

vector<long long> findBetween(const vector<int>& A, const vector<int>& B) {
    long long L = findLCM(A);
    long long G = findGCD(B);

    vector<long long> res;
    if (L > G) return res;

    for (long long x = L; x <= G; x += L) {
        if (G % x == 0) {
            res.push_back(x);
        }
    }
    return res;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> A(n), B(m);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < m; i++) cin >> B[i];

    vector<long long> ans = findBetween(A, B);
    cout << ans.size() << "\n";
    for (long long x : ans)
        cout << x << " ";
    return 0;
}
