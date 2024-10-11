#include<bits/stdc++.h>
using namespace std;
int main(){
    int q;
    set<int> s;
    cin >> q;
    while (q--) {
        int i;
        cin>>i;
        s.insert(i);
    }
    if (s.size()<2) {
        cout << "NO" <<"\n";
        return 0;
    }
    q=0;
    for(int x:s) if (q) {
        cout << x << "\n";
        break;
    } else q++;
    return 0;
}