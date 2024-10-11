#include <stdio.h>
typedef long long E;


extern E max_subarray(E n, E l, E r, E a[]);

int main(){
    E n, l, r;
    scanf("%lld %lld %lld", &n, &l, &r);
    E a[n+1];
    a[0] = 0;
    for(E i = 1; i <= n; i++){
        scanf("%lld", &a[i]);
    }

    E ans = max_subarray(n, l, r, a);

    printf("%lld\n", ans);

    return 0;
}