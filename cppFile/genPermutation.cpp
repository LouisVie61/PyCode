// No dublicate

#include <iostream>
#include <vector>
using namespace std;

string s;
vector<string> res;
bool used[100];

void gen(string ans) {
    if ((int) ans.size() == (int) s.size()) {
        res.push_back(ans);
        return;
    }
    
    for (int i = 0; i < (int) s.length(); i++) {
        if (!used[i]) {
            used[i] = true;
            gen(ans + s[i]);
            used[i] = false;
        }
    }
}

int main() {
    cin >> s;
    gen("");
    
    for (auto str : res) {
        cout << str << endl;
    }
}