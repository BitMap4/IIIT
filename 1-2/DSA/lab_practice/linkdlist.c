#include <stdio.h>
#include <stdlib.h>
typedef long long E;

E merge(int arr[], int l, int r, int m) {
    int n1 = (m+1)-l, n2 = r-m;
    int il=0, ir=0, i=l;
    int L[n1], R[n2];
    for (int i=0; i<n1; i++) L[i] = arr[l+i];
    for (int i=0; i<n2; i++) R[i] = arr[m+1+i];

    while (il<n1 && ir<n2) 
        if (L[il] < R[ir]) arr[i++] = L[il++];
        else arr[i++] = R[ir++];

    E ans=0;
    if (il<n1) ans = (E)n2*(E)(n1-il);
    else ans = (E)n1*(E)ir;
    while (il<n1) arr[i++] = L[il++];
    while (ir<n2) arr[i++] = R[ir++];

    // printf("%lld ", ans);
    return ans;
}

E merge_sort(int arr[], int l, int r) {
    if (l<r) {
        int m = l + ((r-l)>>1);
        E left = merge_sort(arr, l, m);
        E right = merge_sort(arr, m+1, r);
        return left + right + merge(arr, l, r, m);
    }
    return 0;
}

int main() {
    int t; scanf("%d", &t);

    while(t--) {
        int n; scanf("%d", &n);
        int arr[n]; for (int i=0; i<n; i++) scanf("%d", &arr[i]);

        E total = merge_sort(arr, 0, n-1);
        // for (int i=1;i<n;i++) if (arr[i-1] == arr[i]) total++;
        printf("%lld\n", total);
    }

    return 0;
}