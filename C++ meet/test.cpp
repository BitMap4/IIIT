#include<bits/stdc++.h>
using namespace std;

void test() {
    //9 8 6 5 4 2
    //6 5 4 3 1 1
    int n;
    cin >> n;
    int a[n], b[n];
    for (int i=0; i<n; i++) cin>>a[i];
    for (int i=0; i<n; i++) cin>>b[i];
    sort(a, a+n);
    sort(b, b+n);
    int ans=1;
    int pos=0;
    for (int i=0; i<n; i++) {
        for(;pos<n;pos++){
            if (a[i] <= b[pos]) break;
        }
        ans=ans*(pos-i) % 1000000007;
    }
    cout << ans << "\n";
}

int main(){
    int t;
    cin >> t;
    while (t--) test();
    return 0;
}