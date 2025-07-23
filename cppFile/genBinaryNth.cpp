// Yêu cầu: Viết chương trình liệt kê tất cả các chuỗi nhị phân có độ dài n
// Input: Một dòng duy nhất chứa số nguyên dương n
// Output: Tất cả các chuỗi nhị phân có độ dài n, 
//         mỗi chuỗi trên 1 dòng, chuỗi có giá trị nhỏ đứng trước.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int n;
vector<string> res;

void gen(string s, int n) {
    if ((int) s.length() == n) {
        res.push_back(s);
        return;
    }

    gen(s + "0", n);
    gen(s + "1", n);
}

int main() {
    cout << "Nhap do dai cua chuoi nhi phan: ";
    cin >> n;

    gen("", n);

    // In ra các chuỗi nhị phân
    for (const string& s : res) {
        cout << s << endl;
    }

    return 0;
}