#include <stdio.h>
#include <stdlib.h>

typedef struct station {
    long long int depth, time;
} Station;
typedef Station* station;

long long int* insert(long long int* heap, long long int pos, long long int c) {
    heap[pos] = c;
    while (pos > 0 && heap[pos] < heap[(pos - 1)/2]) {
        long long int temp = heap[pos];
        heap[pos] = heap[(pos - 1)/2];
        heap[(pos - 1)/2] = temp;
        pos = (pos - 1)/2;
    }
    return heap;
}

long long int* pop(long long int* heap, long long int size) {
    heap[0] = heap[size - 1];
    long long int pos = 0;
    while (2*pos + 1 < size) {
        long long int left = 2*pos + 1;
        long long int right = 2*pos + 2;
        long long int min = pos;
        if (left < size && heap[left] < heap[min]) min = left;
        if (right < size && heap[right] < heap[min]) min = right;
        if (min == pos) break;
        long long int temp = heap[pos];
        heap[pos] = heap[min];
        heap[min] = temp;
        pos = min;
    }
    return heap;
}

int cmp(const void* a, const void* b) {
    return (((*(station*)a)->depth > (*(station*)b)->depth)<<1) - 1;
}

int main() {
    long long int n, available, req_depth, refill, size=0, time=0;
    scanf("%lld%lld%lld%lld", &n, &available, &req_depth, &refill);
    station stations[n];
    for (long long int i = 0; i < n; i++) stations[i] = (station)malloc(sizeof(Station));
    long long int* heap = (long long int*)malloc((n+5) * sizeof(long long int));
    for (long long int i = 0; i < n; i++) scanf("%lld", &stations[i]->depth);
    for (long long int i = 0; i < n; i++) scanf("%lld", &stations[i]->time);

    qsort(stations, n, sizeof(station), cmp);

    // for (long long int i = 0; i < n; i++) {
    //     available -= stations[i]->depth - depth;
    //     depth = stations[i]->depth;
    //     while (available < 0) {
    //         if (size == 0) {
    //             printf("-1 %lld", depth+available);
    //             return 0;
    //         }
    //         available += refill;
    //         time += heap[0];
    //         heap = pop(heap, size--);
    //     }
    //     heap = insert(heap, size++, stations[i]->time);
    // }

    // available -= req_depth - depth;
    // depth = req_depth;
    // while (available < 0) {
    //     if (size == -1) {
    //         printf("-1 %lld", depth+available);
    //         return 0;
    //     }
    //     available += refill;
    //     time += heap[0];
    //     heap = pop(heap, size--);
    // }

    
    int j = 0;
    while (available < req_depth) {
        while (j < n && stations[j]->depth <= available) {
            heap = insert(heap, size++, stations[j]->time);
            j++;
        }
        time += heap[0];
        if (size == 0) {
            printf("-1 %lld", available);
            return 0;
        }
        heap = pop(heap, size--);
        available += refill;
    }

    printf("%lld", time);

    return 0;
}