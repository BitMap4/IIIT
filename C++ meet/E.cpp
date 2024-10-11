#include<bits/stdc++.h>
using namespace std;
int main() {
    int m,n;
    map<string, string> dic;
    cin >> n >> m;
    while(n--) {
        string name,ip;
        cin >> name >> ip;
        dic[ip+";"] = name;
        //cout << "TEST: " << dic[ip+";"] << endl;
    }
    while (m--) {
        string ip, cmd;
        cin >> cmd >> ip;
        cout << cmd <<" "<< ip <<" #"<< dic[ip] << "\n";
    }
    return 0;
}