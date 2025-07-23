#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string s;
vector<string> res;

void gen(string ans, int len) {
    if ((int) ans.size() == len) {
        res.push_back(ans);
        return;
    }
    
    for (int i = 0; i < (int) s.size(); i++) {
        gen(ans + s[i], len);
    }
}

int main() {
    cin >> s;
    for (int i = 1; i <= (int) s.size(); i++) gen("", i);
    
    for (auto str : res) {
        cout << str << endl;
    }
}