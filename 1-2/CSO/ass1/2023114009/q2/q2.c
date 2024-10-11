#include <stdio.h>
typedef long long int ll;

void rot(ll* x, ll size); // the function which is defined in the assembly file- it does all the logic and arithmetic of the program

int main() {
    ll n; // n is the size of the array
    scanf("%lld", &n);
    ll arr[n]; // the arry to be rotated
    for (ll i = 0; i < n; i++) scanf("%lld", &arr[i]);
    rot(arr, n); // rotates the array by 1 to the left
    for (ll i = 0; i < n; i++) printf("%lld ", arr[i]);
}