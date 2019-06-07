#include <bits/stdc++.h>
using namespace std;
string msg, code;
int M, C, TC, freq[300], sol;
vector<string> v, save;
ifstream fcin("compression.in");
void readCase()
{
    getline(fcin, msg);
    getline(fcin, code);
    M = (int)msg.size();
    C = (int)code.size();
    vector<int> lf(256, 0);
    memset(freq, 0, sizeof freq);
    for (int i = M - 1; i >= 0; i--)
    {
        freq[i] = lf[msg[i]], lf[msg[i]]++;
    }
    /*for (int i = 0; i < M; i++)
        cout << freq[i] << " " << lf[msg[i]]<<endl;;/*/
    v.assign(256, "");
    sol = 0;
}
int compare(string a, string b)
{
    if (b.find(a) == 0)
        return -1;
    if (a.find(b) == 0)
        return 0;
    return 1;
}
int can_choose(string choice, int m)
{
    for (int i = 0; i < m; i++)
    {
        int can = compare(v[msg[i]], choice);
        if (can != 1)
            return can;
    }
    return 1;
}
int occurrence(string seq, string text, int i)
{
    i = text.find(seq, i);
    int j = 0;
    while (i != string::npos)
    {
        j++;
        i = text.find(seq, i + 1);
    }
    return j;
}
//backtrack
void find(int m, int c)
{
    if (sol > 1)
        return;
    if (m == M && c == C)
    {
        sol++;
        save = v;
    }
    if (m > M || c > C)
        return;
    if (v[msg[m]] == string(""))
    {
        for (int i = 1; i <= C - c; i++)
        {
            string substr = code.substr(c, i);
            //printf("sub %c = %s\n", msg[m], substr.c_str());
            if (occurrence(substr, code, c + i) < freq[m])
                return;
            int can = can_choose(substr, m);
            if (can == -1)
                return;
            if (can)
            {
                v[msg[m]] = substr;
                find(m + 1, c + i);
                v[msg[m]] = "";
            }
        }
    }
    else
    {
        string substr = v[msg[m]];
        for (int i = 0; i < substr.size(); i++)
            if (substr[i] != code[c + i])
                return;
        if (occurrence(substr, code, c+substr.size()) < freq[m])
            return;
        find(m + 1, c + substr.size());
    }
}
void print_sol()
{
    if (sol > 1)
        cout << "MULTIPLES DATABASES" << endl;
    else
    {
        sort(msg.begin(), msg.end());
        bitset<256> doing;
        for (int i = 0; i < M; i++)
            if (!doing[msg[i]])
            {
                printf("%c = %s\n", msg[i], save[msg[i]].c_str());
                doing.set(msg[i]);
            }
    }
}
int main()
{
    fcin >> TC;
    fcin.ignore();
    int tt = 1;
    while (TC--)
    {
        cout << "DATASET #" << tt++ << endl;
        readCase();
        find(0, 0);
        print_sol();
    }
}