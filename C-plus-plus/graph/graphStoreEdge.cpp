#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    // u -> v
    int u, v;
};

int n, m;

vector<Edge> edges;
vector<bool> vis;


bool findEdge(int u, int v) {
    for (const auto & edge : edges) {
        if(edge.u == u && edge.v == v) {
            return true;
        }
    }
    return false;
}

void dfs(int u) {
    // avoid repeatedly visiting a node
    if (vis[u] == true) return;
    vis[u] = true;
    // find the edge
    for (const auto & edge : edges) {
        if(edge.u == u) {
            dfs(edge.v);
        }
    }
}