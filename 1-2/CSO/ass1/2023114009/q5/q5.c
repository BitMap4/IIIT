#include <stdio.h>
#include <stdlib.h>
typedef long long int ll;

void prod(ll* arr, ll n, ll* new);

ll main(){
    ll n;
    scanf("%lld", &n);
    ll arr[n], new[n];
    for (ll i = 0; i < n; i++) scanf("%lld", &arr[i]);
    prod(arr, n, new);
    for (ll i = 0; i < n; i++) printf("%lld ", new[i]);
    return 0;
}