#include <stdio.h>
typedef long long E;

extern void binary_s(E x, E result[], E arr[]);

int main() {
    E arr[32], result[2], x;
    for (E i=0; i<32; i++) {
        scanf("%lld", &arr[i]);
    }
    scanf("%lld", &x);
    binary_s(x, result, arr);
    printf("%lld %lld\n", result[0], result[1]);
    return 0;
}