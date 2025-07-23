// Yêu cầu: Viết chương trình liệt kê tất cả các chuỗi nhị phân có độ dài n chữ số 0 và m chữ số 1.
// Input: Một dòng duy nhất chứa số 2 số nguyên dương n và m.
// Output:
// Tất cả các chuỗi nhị phân có độ dài n chữ số 0 và m chữ số 1, mỗi chuỗi trên 1 dòng, chuỗi có giá trị nhỏ đứng trước.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int n, m;
vector<string> res;

void gen(string s, int cnt0, int cnt1) {
    int totalLength = n + m;
    
    if ((int) s.length() == totalLength) {
        res.push_back(s);
        return;
    }
    
    if (cnt0 < n) {
        gen(s + "0", cnt0 + 1, cnt1);
    }
    
    if (cnt1 < m) {
        gen(s + "1", cnt0, cnt1 + 1);
    }
}

int main() {
    cin >> n >> m;
    
    gen("", 0, 0);
    
    for (auto str : res) {
        cout << str << endl;
    }
}