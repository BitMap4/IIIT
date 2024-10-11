#include <stdio.h>
#include <stdlib.h>

typedef struct Chamber {
    int required, available;
} Chamber;
typedef Chamber* chamber;

chamber* insert(chamber* heap, int pos, chamber c) {
    heap[pos] = (chamber)malloc(sizeof(Chamber));
    heap[pos]->available = c->available;
    heap[pos]->required = c->required;
    while (pos > 0 && heap[pos]->required > heap[(pos - 1)/2]->required) {
        chamber temp = heap[pos];
        heap[pos] = heap[(pos - 1)/2];
        heap[(pos - 1)/2] = temp;
        pos = (pos - 1)/2;
    }
    return heap;
}

chamber* pop(chamber* heap, int end) {
    heap[0] = heap[end - 1];
    int pos = 0;
    while (2*pos + 1 < end) {
        int left = 2*pos + 1;
        int right = 2*pos + 2;
        int max = pos;
        if (left < end && heap[left]->required > heap[max]->required) max = left;
        if (right < end && heap[right]->required > heap[max]->required) max = right;
        if (max == pos) break;
        chamber temp = heap[pos];
        heap[pos] = heap[max];
        heap[max] = temp;
        pos = max;
    }
    return heap;
}

int main() {
    int n, k, possible=1;
    scanf("%d%d", &n, &k);
    chamber* chambers = (chamber*)malloc(n * sizeof(chamber));
    chamber* positive = (chamber*)malloc(n * sizeof(chamber));
    chamber* negative = (chamber*)malloc(n * sizeof(chamber));
    for (int i = 0; i < n; i++) chambers[i] = (chamber)malloc(sizeof(Chamber));
    for (int i = 0; i < n; i++) positive[i] = (chamber)malloc(sizeof(Chamber));
    for (int i = 0; i < n; i++) negative[i] = (chamber)malloc(sizeof(Chamber));
    for (int i = 0; i < n; i++) scanf("%d", &(chambers[i]->required));
    for (int i = 0; i < n; i++) scanf("%d", &(chambers[i]->available));
    int p = 0, q = 0;
    
    for (int i = 0; i < n; i++) {
        if (chambers[i]->available <= 0) {
            negative = insert(negative, q, chambers[i]);
            q++;
        } else {
            chambers[i]->required = -chambers[i]->required;
            positive = insert(positive, p, chambers[i]);
            chambers[i]->required = -chambers[i]->required;
            p++;
        }
    }

    // for (int i = 0; i < p; i++) printf("%d ", positive[i]->required);
    // printf("\n");
    // for (int i = 0; i < q; i++) printf("%d ", negative[i]->required);
    // printf("\n\n");

    while (p) {
        if (k < -positive[0]->required) {
            possible = 0;
            break;
        k += positive[0]->available;
        }
        positive = pop(positive, p--);
        // for (int i = 0; i < p; i++) printf("%d ", positive[i]->required);
        // printf("\n");
    }
    // printf("\n");

    if (possible) 
    while (q) {
        if (k < negative[0]->required) {
            possible = 0;
            break;
        }
        k += negative[0]->available;
        negative = pop(negative, q--);
        // for (int i = 0; i < q; i++) printf("%d ", negative[i]->required);
        // printf("\n");
    }

    (possible && k>=0) ? printf("YES") : printf("NO");
    // printf("\n %d %d %d", k, p, q);

    return 0;
}