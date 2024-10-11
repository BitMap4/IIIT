#include<stdio.h>
typedef long long int ll;

ll check(ll* str, ll n) ;

int main() {
    ll n;
    scanf("%lld", &n);
    ll arr[n];
    scanf("%*c");
    for (ll i = 0; i < n; i++) {
        char c;
        scanf("%c", &c);
        arr[i] = (ll)c;
    }
    printf("%lld\n", check(arr, n));
    return 0;
}