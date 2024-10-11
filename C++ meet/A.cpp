#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin >> s;
    int counter = 0;
    for (int i = s.size()-1; i > -1; i--){
        if (s[i] == '<') {
            counter++;
            s = s.substr(0, i) + s.substr(i+1, s.size());
        }
        else if (s[i] != '<' && counter != 0) {
            counter--;
            s = s.substr(0, i) + s.substr(i+1, s.size());
        }
    }
    cout << s << "\n";
    return 0;
}