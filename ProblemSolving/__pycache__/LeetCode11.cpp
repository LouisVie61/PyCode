#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
using namespace std;

int solve(int a[], int n) {
    vector<pair<int, int>> container;

    for (int i = 0; i < n; ++i) {
        container.push_back({a[i], i});
    }
    
    int left = 0, right = n - 1;
    int maxWater = 0;

    while (left <= right) {
        int height = min(container[left].first, container[right].first);
        int width = abs(container[right].second - container[left].second);
        maxWater = max(maxWater, height * width);

        if (container[left].first < container[right].first) {
            left++;
        } else {
            right--;
        }
    }

    return maxWater;
}

int main() {
    int n; cin >> n;
    int a[n];
    rep(i, 0, n) cin >> a[i];

    cout << "Max amount of water: " << solve(a, n) << endl;
}