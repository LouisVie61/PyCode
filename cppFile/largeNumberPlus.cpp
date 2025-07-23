#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string plusBigNumbers(string a, string b) {
    // Đảm bảo chuỗi a ngắn hơn hoặc bằng b
    if (a.length() > b.length()) swap(a, b);

    // Đảo ngược cả hai chuỗi
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    string result = "";
    int carry = 0;

    // Cộng từng chữ số
    for (int i = 0; i < a.length(); i++) {
        int sum = (a[i] - '0') + (b[i] - '0') + carry;
        result.push_back((sum % 10) + '0');
        carry = sum / 10;
    }

    // Xử lý phần còn lại của chuỗi b
    for (int i = a.length(); i < b.length(); i++) {
        int sum = (b[i] - '0') + carry;
        result.push_back((sum % 10) + '0');
        carry = sum / 10;
    }

    // Nếu còn dư
    if (carry) result.push_back(carry + '0');

    // Đảo ngược kết quả để trả về đúng thứ tự
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    string num1, num2;
    cout << "Nhap so thu nhat: ";
    cin >> num1;
    cout << "Nhap so thu hai: ";
    cin >> num2;

    string sum = plusBigNumbers(num1, num2);
    cout << "Tong = " << sum << endl;
    return 0;
}
