#include <stdio.h>
#include <stdlib.h>

typedef struct Chamber {
    unsigned long long int required;
    long long int available;
} Chamber;
typedef Chamber* chamber;

int cmp1(const void* a, const void* b) {
    unsigned long long int val_a = (*(const chamber*)a)->required;
    unsigned long long int val_b = (*(const chamber*)b)->required;
    if (val_a == val_b) {
        return (*(const chamber*)a)->available - (*(const chamber*)b)->available;
    }
    return ((val_a > val_b)<<1) - 1;
}

int cmp2(const void* a, const void* b) {
    return -cmp1(a, b);
}

int main() {
    long long int n, available;
    scanf("%lld%lld", &n, &available);
    chamber* chambers = (chamber*)malloc(n * sizeof(chamber));
    for (long long int i = 0; i < n; i++) chambers[i] = (chamber)malloc(sizeof(Chamber));
    for (long long int i = 0; i < n; i++) scanf("%llu", &(chambers[i]->required));
    long long int p = 0, q = 0;
    for (long long int i = 0; i < n; i++) {
        scanf("%lld", &(chambers[i]->available));
        if (chambers[i]->available >= 0) p++;
        else q++;
    }

    chamber* positive = (chamber*)malloc(p * sizeof(chamber));
    chamber* negative = (chamber*)malloc(q * sizeof(chamber));
    for (long long int i = 0; i < p; i++) positive[i] = (chamber)malloc(sizeof(Chamber));
    for (long long int i = 0; i < q; i++) negative[i] = (chamber)malloc(sizeof(Chamber));

    for (long long int i = 0, j = 0, k = 0; i < n; i++) {
        if (chambers[i]->available > 0) positive[j++] = chambers[i];
        else negative[k++] = chambers[i];
    }

    qsort(positive, p, sizeof(chamber), cmp1);
    qsort(negative, q, sizeof(chamber), cmp2);

    for (long long int i = 0; i < p; i++) {
        if (positive[i]->required > available) {
            printf("NO");
            return 0;
        }
        available += positive[i]->available;
    }

    for (long long int i = 0; i < q; i++) {
        if (negative[i]->required > available) {
            printf("NO");
            return 0;
        }
        available += negative[i]->available;
    }

    for (long long int i = 0; i < n; i++) free(chambers[i]);

    (available >= 0) ? printf("YES") : printf("NO");
    // printf("\n %lld %lld %lld", k, p, q);

    return 0;
}
