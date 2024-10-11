#include<bits/stdc++.h>
using namespace std;
int main(){
    int q;
    set<int> s;
    cin >> q;
    while (q--){
        int a, b;
        cin >> a >> b;
        if (a == 1) s.insert(b);
        else if (a == 2) s.erase(b);
        else if (a == 3) {
            if (s.find(b) != s.end()) cout << "Yes\n";
            else cout << "No\n";
        }
    }
    return 0;
}