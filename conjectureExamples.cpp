#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ll r; cin >> r;
    unordered_map<ll, ll> dp(r+1);
    dp[1] = 1;
    for(ll i=2; i<=r; i++) {
        ll n = i;
        ll steps = 0;
        while(n >= 1) {
            if(dp.count(n)) {
                steps += dp[n];
                break;
            }
            if(n & 1) {
                n = (n*3+1)>>1;
                steps += 2;
            } else {
                n >>= 1;
                steps++;
            }
        }
        dp[i] = steps;
    }
    cout << "All numbers work!" << endl;
    cout << dp[r] << endl;
    return 0;
}