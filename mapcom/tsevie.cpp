#include <bits/stdc++.h>
using namespace std;
const int N = 100;
char grid[N][N];
int dx[] = {-1, 1, 0, 0, -1, 1, 1, -1};
int dy[] = {0, 0, -1, 1, -1, -1, 1, 1};
int n, m, k;
struct Node
{
    int x, y, w;
};
queue<Node> Fires, Kokous;
int expand()
{
    int actual_pos = Kokous.size();
    for (int i = 0; i < actual_pos; i++)
    {
        Node node = Kokous.front();
        Kokous.pop();
        //printf("node(%d,%d,%d)\n", node.x, node.y, node.w);
        for (int j = 0; j < 4; j++)
        {
            int Nx = node.x + dx[j], Ny = node.y + dy[j];
            if (Nx >= 0 && Nx < m && Ny >= 0 && Ny < n)
            {
                //printf("child node(%d,%d)->%c\n", Nx, Ny, grid[Ny][Nx]);
                if (grid[Ny][Nx] == 't')
                    return node.w + 1;
                if (grid[Ny][Nx] == '-')
                {
                    Kokous.push(Node{Nx, Ny, node.w + 1});
                    grid[Ny][Nx] = '#';
                }
            }
        }
    }
    return 0;
}
void fire()
{
    int actual_fire = Fires.size();
    for (int i = 0; i < actual_fire; i++)
    {
        Node node = Fires.front();
        Fires.pop();
        for (int j = 0; j < 8; j++)
        {
            int Nx = node.x + dx[j], Ny = node.y + dy[j];
            if (Nx >= 0 && Nx < m && Ny >= 0 && Ny < n && grid[Ny][Nx] != 'f')
            {
                Fires.push(Node{Nx, Ny, 0});
                grid[Ny][Nx] = 'f';
            }
        }
    }
}
int main()
{
    //ifstream cin("in");
end:
    while (cin >> n >> m >> k && (n + m + k))
    {
        while (!Fires.empty())
            Fires.pop();
        while (!Kokous.empty())
            Kokous.pop();
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cin >> grid[i][j];
                if (grid[i][j] == 'f')
                    Fires.push(Node{j, i, 0});
                else if (grid[i][j] == 's')
                    Kokous.push(Node{j, i, 0});
                //else if (grid[i][j] == 't')
                //printf("obj (%d,%d)->%c\n", j, i, grid[i][j]);
            }
        }
        int time = 1;
        while (!Kokous.empty())
        {
            if (time % k == 0)
                fire();
            int ans = expand();
            //cout << "ans" << ans << endl;
            if (ans)
            {
                cout << ans << endl;
                goto end;
            }
            time++;
        }
        cout<< "Impossible" << endl;
        //return 0;
    }
    return 0;
}