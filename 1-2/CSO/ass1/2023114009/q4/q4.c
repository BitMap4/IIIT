#include <stdio.h>
typedef long long int ll;

ll sum(ll* arr, ll n);

int main(){
    ll n;
    scanf("%lld", &n);
    ll arr[n];
    for (ll i = 0; i < n; i++) scanf("%lld", &arr[i]);
    printf("%lld\n", sum(arr, n));
    return 0;
}