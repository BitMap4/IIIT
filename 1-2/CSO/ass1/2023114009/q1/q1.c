#include <stdio.h>
typedef long long int ll;

void execute(ll* x, ll curr); // the function which is defined in the assembly file- it does all the logic and arithmetic of the program

int main() {
    ll n, ans=0; // n is the size of the array and ans will store the final answer
    scanf("%lld", &n);
    for (ll i = 0; i < 2*n+1; i++) {
        ll curr;
        scanf("%lld", &curr);
        execute(&ans, curr); // performs ans^curr and stores it in ans
    }
    printf("%lld\n", ans); // now ans = xor(arr[1], arr[2] ... arr[n]), and since a^a=0, all pairs will cancel each other to become 0, and the lonely number will be left since b^0=b
    return 0;
}