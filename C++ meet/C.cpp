#include<bits/stdc++.h>
using namespace std;
int main(){
    map<string,int> m;
    int q;
    cin >> q;
    while(q--) {
        int i;
        string name;
        cin >> i >> name;
        if (i==1) {
            int marks;
            cin >> marks;
            m[name]+=marks;
        } else if (i==2) m.erase(name);
        else cout << m[name] << "\n";
    }
    return 0;
}