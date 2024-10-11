#include <bits/stdc++.h>
using namespace std;
typedef long long E;

typedef struct triplet {
    int node, weight;
    bool removable;
} triplet;

int main() {
    int n, normal, fibre;
    cin >> n >> normal >> fibre;
    vector<triplet> adj[n];
    for (int i = 0; i < normal; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        if (a==b) continue;
        a--; b--;
        bool found = false;
        for (int j = 0; j < adj[a].size(); j++) {
            if (adj[a][j].node == b) {
                adj[a][j].weight = min(adj[a][j].weight, w);
                for (int k = 0; k < adj[b].size(); k++) {
                    if (adj[b][k].node == a) {
                        adj[b][k].weight = min(adj[b][k].weight, w);
                    }
                }
                found = true;
                break;
            }
        }
        if (!found) {
            adj[a].push_back({b, w, false});
            adj[b].push_back({a, w, false});
        }
    }
    for (int i = 0; i < fibre; i++) {
        int a, w;
        cin >> a >> w;
        a--;
        bool found = false;
        for (int j = 0; j < adj[0].size(); j++) {
            if (adj[0][j].node == a) {
                if (adj[0][j].weight > w) {
                    adj[0][j].weight = w;
                    adj[0][j].removable = true;
                    for (int k = 0; k < adj[a].size(); k++) {
                        if (adj[a][k].node == 0) {
                            adj[a][k].weight = w;
                            adj[a][k].removable = true;
                        }
                    }
                }
                found = true;
            }
            
        }
        if (!found) {
            adj[a].push_back({0, w, true});
            adj[0].push_back({a, w, true});
        }
    }

    vector<E> dist(n, INT64_MAX);
    vector<bool> used_fibre(n, false);
    vector<bool> visited(n, false);
    dist[0] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 0});
    while (!pq.empty()) {
        pair<int, int> p = pq.top();
        pq.pop();
        if (visited[p.second]) continue;
        visited[p.second] = true;
        int u = p.second;
        for (auto edge : adj[u]) {
            E D = dist[u] + edge.weight;
            if (!visited[edge.node] && dist[edge.node] > D) {
                dist[edge.node] = D;
                pq.push({dist[edge.node], edge.node});
                if (edge.removable) {
                    used_fibre[edge.node] = true;
                } else used_fibre[edge.node] = false;
            } 
            else if (!visited[edge.node] && dist[edge.node] == D) {
                if (edge.removable) {
                    used_fibre[edge.node] = true;
                } else used_fibre[edge.node] = false;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (used_fibre[i]) fibre--;
    }
    cout << fibre << endl;

    return 0;
}