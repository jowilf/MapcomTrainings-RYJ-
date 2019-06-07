#include <bits/stdc++.h>
using namespace std;
const int N = 100000;
char store[] = "00000";
unordered_map<string, bool> maps;
void find(string s, int pos = 0, int v = 0)
{
    if (pos == s.size())
    {
        //printf("Found for %s\n", string(store).substr(0, s.size()).c_str());
        maps[string(store).substr(0, s.size())] = true;
        return;
    }
    else if (pos == 0)
    {
        int l = '0' - s[pos];
        int r = '9' - s[pos];
        for (int i = l; i <= r; i++)
            if (i != 0)
            {
                store[pos] = s[pos] + i;
                find(s, pos + 1, i);
            }
    }
    else
    {
        int l = '0' - s[pos];
        int r = '9' - s[pos];
        if (l <= v && r >= v)
        {
            store[pos] = s[pos] + v;
            find(s, pos + 1, v);
        }
        if (l <= -v && r >= -v)
        {
            store[pos] = s[pos] - v;
            find(s, pos + 1, v);
        }
    }
}
int main()
{
    //ifstream cin("in");
    int T, n, nbr, tt = 1;
    string in;
    cin >> T;
    while (T--)
    {
        nbr = 0;
        maps.clear();
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> in;
            //cout << "read " << in << endl;
            unordered_map<string, bool>::iterator it = maps.find(in);
            if (it == maps.end())
            {
                find(in);
                maps[in] = true;
                nbr += 1;
            }
        }
        printf("Case %d: %d\n", tt++, nbr);
    }
}