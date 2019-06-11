#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long ll;
const ll INF = 1e18;
struct Edge
{
    int u, v;
    ll c, f; //capacity-flow
    Edge(int _u, int _v, ll _c) : u(_u), v(_v), c(_c), f(0) {}
};
class NF //Network flow Edmonds Karp's algorithm
{
private:
    int V;
    vector<vi> adjList;
    vector<Edge> edges;
    vector<ii> path;
    vi dist, last;

    bool bfs(int s, int t)
    {
        dist.assign(V, -1), dist[s] = 0;
        queue<int> q({s});
        path.assign(V, ii(-1, -1));
        while (!q.empty())
        {
            int u = q.front();
            q.pop();
            if (u == t)
                break;
            for (auto idx : adjList[u])
            {
                Edge edge = edges[idx];
                if ((edge.c - edge.f > 0) && dist[edge.v] == -1)
                {
                    dist[edge.v] = dist[u] + 1;
                    q.push(edge.v);
                    //printf("push %d in q\n", edge.v);
                    path[edge.v] = ii(u, idx);
                }
            }
        }
        //printf("dist t %d\n", dist[t]);
        return dist[t] != -1;
    }
    ll dfs(int s, int t, ll f = INF)
    {
        if (s == t || f == 0)
            return f;
        for (int &i = last[s]; i < adjList[s].size(); ++i)
        {
            Edge *edge = &edges[adjList[s][i]];
            if (dist[edge->v] == dist[edge->u] + 1)
                if (ll flow_to_push = dfs(edge->v, t, min(f, edge->c - edge->f)))
                {
                    edge->f += flow_to_push;
                    Edge *bEdge = &edges[adjList[s][i] ^ 1];
                    bEdge->f -= flow_to_push;
                    return flow_to_push;
                }
        }
        return 0;
    }

    ll send_one_flow(int s, int t, ll f = INF)
    {
        if (s == t)
            return f;
        int u = path[t].first, idx = path[t].second;
        Edge *edge = &edges[idx];
        ll flow_to_push = send_one_flow(s, u, min(f, edge->c - edge->f));
        edge->f += flow_to_push;
        Edge *bEdge = &edges[idx ^ 1]; //back edge
        bEdge->f -= flow_to_push;
        //printf("pushed to %d(%d,%d)-(%d-%d)\n", flow_to_push, edge->u, edge->v, bEdge->u, bEdge->v);
        return flow_to_push;
    }

public:
    NF(int _V) : V(_V)
    {
        edges.clear();
        adjList.assign(V, vi());
    }
    void add_edge(int u, int v, int c)
    {
        edges.push_back(Edge(u, v, c));
        adjList[u].push_back(edges.size() - 1);
        //Edge edge = edges.back();
        //printf("Add edge %d->%d with %d\n", edge.u, edge.v, edge.c);
        edges.push_back(Edge(v, u, 0));
        adjList[v].push_back(edges.size() - 1);
        //edge = edges.back();
        //printf("Add edge %d->%d with %d\n", edge.u, edge.v, edge.c);
    }

    ll find_max_flow(int s, int t, int d)
    {
        ll mf = 0;
        while (bfs(s, t))
        {
            ll f = send_one_flow(s, t);
            if (f == 0)
                break;
            mf += f;
            if (mf == d)
                return mf;
        }
        return mf;
    }
    ll dinic(int s, int t, int d)
    {
        ll mf = 0;
        while (bfs(s, t))
        {
            last.assign(V, 0);
            while (ll f = dfs(s, t))
            {
                mf += f;
                if (mf == d)
                    return mf;
            }
        }
        return mf;
    }
};
const int N = 500 + 2;
ll pA[N];
vi bus[N];
int main()
{
    //freopen("C:\\Users\\Jocelin\\PycharmProjects\\MAPC\\InOut\\contest.in", "r", stdin);
    freopen("contest.in", "r", stdin);
    int n, d, p, V, t, m, x, s = 0;
    while (cin >> n >> d >> p && (n))
    {
        memset(pA, 0, sizeof pA);
        //memset(r, 0, sizeof r);
        for (int i = 1; i <= d; i++)
        {
            cin >> m;
            bus[i].clear();
            for (int j = 0; j < m; j++)
            {
                cin >> x;
                bus[i].push_back(x);
                pA[x] += p / m;
            }
        }
        V = (n + d + 2), t = V - 1;
        // binary search for unfairness
        ll left = 0, right = (ll)p * d;
        while (left < right)
        {
            ll mid = (left + right) / 2;
            NF nf = NF(V);
            for (int i = 1; i <= n; i++)
                nf.add_edge(s, i, min((ll)d, (mid + pA[i]) / p));
            for (int i = 1; i <= d; i++)
            {
                nf.add_edge(n + i, t, 1);
                for (int x : bus[i])
                    nf.add_edge(x, n + i, 1);
            }
            if (nf.dinic(s, t, d) == d)
                right = mid;
            else
                left = mid + 1;
        }
        printf("%lld\n", left);
    }
    return 0;
}