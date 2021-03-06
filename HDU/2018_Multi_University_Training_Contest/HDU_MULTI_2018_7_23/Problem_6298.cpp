#include <bits/stdc++.h>
#pragma optimize("Ofast")
using namespace std;
typedef long long ll;
#define rep(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define _rep(i, n) for (int (i) = 1; (i) <= (n); (i)++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define square(x) ((x) * (x))

#ifdef VinceBlack
#define _debug(...) fprintf(stderr, __VA_ARGS__);
#else
#define _debug(...) ;
#endif

signed main()
{
#ifdef Yee_172
    freopen("../in.txt", "r", stdin);
    freopen("../out.txt", "w", stdout);
    time_t __START__ = clock();
#endif
    int t;
    ll n, res;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%lld", &n);
        res = -1;
        if (n % 3 == 0) n /= 3, res = square(n) * n;
        else if (n % 4 == 0) n /= 4, res = square(n) * n * 2;
        printf("%lld\n", res);
    }
#ifdef Yee_172
    time_t __END__ = clock();
    fprintf(stderr, "TOTAL TIME: %.12f ms\n", (__END__ - __START__) / (double)CLOCKS_PER_SEC * 1000);
#endif
    return 0;
}
