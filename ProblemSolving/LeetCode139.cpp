#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for (int i = (a); i < (b); ++i)

bool solve(string s, vector<string> wordDict) {
    vector<bool> dp(s.length() + 1, false);
    dp[s.length()] = true;
    
    for (int i = s.length() - 1; i > -1; i--) {
        for (auto word : wordDict) {
            if ((i + word.length()) <= s.length() && s.substr(i, word.length()) == word) {
                dp[i] = dp[i + word.length()];
            }
            
            if (dp[i]) {
                break;
            }
        }
    }
    
    return dp[0];
}

int main() {
    string s; cin >> s;
    int n; cin >> n;
    vector<string> wordDict(n);
    rep(i,0,n) cin >> wordDict[i];
    
    if (solve(s, wordDict)) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }
}