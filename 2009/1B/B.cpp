 // The Next Number
 // https://code.google.com/codejam/contest/186264/dashboard#s=p1

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int tcs;
    string num;

    cin >> tcs;
    for (int tc = 0; tc < tcs; ++tc)
    {
        cin >> num;
        if (!next_permutation(num.begin(), num.end()))
        {
            size_t nz = num.find_first_not_of('0');
            swap(num[0], num[nz]);
            num.insert(1, "0");
        }

        cout << "Case #" << tc + 1 << ": " << num << endl;
    }

    return 0;
}