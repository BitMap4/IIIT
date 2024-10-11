#include <bits/stdc++.h>
using namespace std;

vector<int> visited (100005, 0);

void dfs(vector<set<int>>& adj, int v) {
    visited[v] = 1;
    for (auto i : adj[v]) {
        if (visited[i] == 0) {
            dfs(adj, i);
        }
    }
}

int main() {
    int m, n, a, b;
    cin >> n >> m;

    vector<set<int>> adj (n);
    for (int i = 0; i < n; i++) adj[i].insert(i);
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a-1].insert(b-1);
        adj[b-1].insert(a-1);
    }

    stack<int> s;
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            s.push(i);
            dfs(adj, i);
        }
    }

    cout << s.size()-1 << '\n';
    while (s.size() > 1) {
        cout << s.top()+1 << " ";
        s.pop();
        cout << s.top()+1 << '\n';
    }

    return 0;
}