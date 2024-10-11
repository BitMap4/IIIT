#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    int cities[n], towers[m];
    for(int i=0;i<n;i++) cin>>cities[i];
    int max_dist = 1000000000; // 10^9
    // find the minimum radius r that each tower needs to cover so all cities are covered
    for(int i=0;i<m;i++) cin>>towers[i];
    for(int i=0;i<n;i++){
        int min_dist = 1000000000;
        for(int j=0;j<m;j++){
            int dist = abs(cities[i]-towers[j]);
            if(dist<min_dist) min_dist = dist;
        }
        if(min_dist<max_dist) max_dist = min_dist;
    }
}