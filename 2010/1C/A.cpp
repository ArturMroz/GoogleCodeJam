#include <iostream>
using namespace std;

int main()
{
    int tcs, n;
    cin >> tcs;
    for (int tc = 0; tc < tcs; ++tc)
    {
        cin >> n;
        int a[n][2], ans = 0;
        
        for (int i = 0; i < n; ++i)
        {
            cin >> a[i][0] >> a[i][1];
        }

        for (int i = 0; i < n; ++i)
        {
            for (int j = i + 1; j < n; ++j)
            {
                ans += (a[i][0] - a[j][0]) * (a[i][1] - a[j][1]) < 0;
            }
        }

        cout << "Case #" << tc + 1 << ": " << ans << endl;
    }

    return 0;
}