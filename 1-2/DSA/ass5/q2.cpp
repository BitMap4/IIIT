#include <bits/stdc++.h>
using namespace std;
typedef long long E;

typedef struct triplet {
    E node, weight;
    bool removable;
} triplet;

int main() {
    E n, normal, fibre;
    cin >> n >> normal >> fibre;
    vector<map<E, triplet>> adj(n);
    for (E i = 0; i < normal; i++) {
        E a, b, w;
        cin >> a >> b >> w;
        if (a==b) continue;
        a--; b--;
        if (adj[a].count(b)) {
            adj[a][b].weight = min(adj[a][b].weight, w);
            adj[b][a].weight = min(adj[b][a].weight, w);
        } else {
            adj[a][b] = {b, w, false};
            adj[b][a] = {a, w, false};
        }
    }
    for (E i = 0; i < fibre; i++) {
        E a, w;
        cin >> a >> w;
        a--;
        if (adj[0].count(a)) {
            E smallest = min(adj[0][a].weight, w);
            if (smallest == w) {
                adj[0][a].weight = smallest;
                adj[a][0].weight = smallest;
                adj[0][a].removable = true;
                adj[a][0].removable = true;
            }
        } else {
            adj[0][a] = {a, w, true};
            adj[a][0] = {0, w, true};
        }
    }

    vector<E> dist(n, INT64_MAX);
    vector<bool> used_fibre(n, false);
    vector<bool> visited(n, false);
    dist[0] = 0;
    priority_queue<pair<E, E>, vector<pair<E, E>>, greater<pair<E, E>>> pq;
    pq.push({0, 0});
    while (!pq.empty()) {
        pair<E, E> p = pq.top();
        pq.pop();
        if (visited[p.second]) continue;
        visited[p.second] = true;
        E u = p.second;
        for (auto it : adj[u]) {
            triplet edge = it.second;
            E D = dist[u] + edge.weight;
            if (dist[edge.node] > D) {
                dist[edge.node] = D;
                pq.push({dist[edge.node], edge.node});
                if (edge.removable) {
                    used_fibre[edge.node] = true;
                } else used_fibre[edge.node] = false;
            } 
            else if (dist[edge.node] == D) {
                if (edge.removable) {
                    used_fibre[edge.node] = true;
                } else used_fibre[edge.node] = false;
            }
        }
    }

    for (E i = 0; i < n; i++) {
        if (used_fibre[i]) fibre--;
    }
    cout << fibre << endl;

    return 0;
}