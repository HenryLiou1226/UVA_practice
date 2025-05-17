#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"
#define IOS                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);
#define me(x) memset(x, 0x3F, sizeof(x))
#pragma GCC optimize("Ofast")
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
int ans = 0;
int solve(int a,int turn)
{
    if(a == 1)
    {
        return turn;
    }
    if(a % 2 == 1)
    {
        solve(a * 3 + 1, turn + 1);
    }
    else
    {
        solve(a / 2, turn + 1);
    }
}
signed main()
{
    IOS;
    int a,b;
    while(cin >> a >> b)
    {
        cout << a << " " << b << " ";
        ans = 0;
        if(a > b)
        {
            swap(a, b);
        }
        for(int i = a; i <= b; i++)
        {
            ans = max(ans, solve(i, 1));
        }
        cout << ans << endl;
    }
}