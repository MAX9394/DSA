#include <bits/stdc++.h>
using namespace std;

void pattern(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}
int main() {
    int t;
    cin >> t;
    pattern(t);
    return 0;
}