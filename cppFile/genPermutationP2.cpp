#include <iostream>
#include <vector>
#include <string>
using namespace std;

string s;
vector<string> res;

void gen(string ans) {
    int n = (int) ans.size();
    
    if (n >= 2 && n <= 3) {
        res.push_back(ans);
    }
    
    if (n == 3) {
        return;
    }
    
    for (int i = 0; i < (int)s.size(); i++) {
        gen(ans + s[i]);
    }
}

int main() {
    cin >> s;
    gen("");
    
    for (auto str : res) {
        cout << str << " ";
    }
}