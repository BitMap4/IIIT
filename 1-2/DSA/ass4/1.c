#include <stdio.h>
#include <stdlib.h>

typedef struct Chamber {
    unsigned long long int required;
    long long int available;
} Chamber;
typedef Chamber* chamber;

int cmp(const void* a, const void* b) {
    return (*(const chamber*)a)->required - (*(const chamber*)b)->required;
}

int main() {
    int n, available, possible=1;
    scanf("%d%d", &n, &available);

    chamber chambers[n];
    for (int i = 0; i < n; i++) chambers[i] = (chamber)malloc(sizeof(Chamber));

    for (int i = 0; i < n; i++) scanf("%llu", &(chambers[i]->required));
    for (int i = 0; i < n; i++) scanf("%lld", &(chambers[i]->available));

    qsort(chambers, n, sizeof(chamber), cmp);

    for (int i=0; i<n; i++) if (chambers[i]->available > 0) {
        if (chambers[i]->required > available) {
            possible = 0;
            break;
        }
        available += chambers[i]->available;
    }

    if(possible)
    for (int i=n-1; i>=0; i--) if (chambers[i]->available <= 0) {
        if (chambers[i]->required > available) {
            possible = 0;
            break;
        }
        available += chambers[i]->available;
    }

    (possible && available >= 0) ? printf("YES") : printf("NO");
    return 0;
}