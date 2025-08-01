#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> a(n); for (auto i = 0; i < n; i++) {
        cin >> a[i];
    }

    int end_index = 0, maxLen = 1;
    vector<int> dp(n, 1), track(n, -1);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                track[i] = j;
            }
        }

        if (dp[i] > maxLen) {
            maxLen = dp[i];
            end_index = i;
        }
    }

    vector<int> res;
    while (end_index != -1) {
        res.push_back(a[end_index]);
        end_index = track[end_index];
    }

    for (auto num : res) {
        cout << num << " ";
    }
}