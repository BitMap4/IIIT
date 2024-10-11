#include <stdio.h>
typedef long long E;

extern E execute(E n, E operations[]);

int main() {
    E n;
    scanf("%lld", &n);
    scanf("%*c");
    E operations[1+n/2];  
    int i=0;
    char c;
    while (scanf("%c", &c)) {
        if (c == '\n') break;
        if (c == ' ') continue;
        operations[i] = (E) ((c<='9' && c>='0') ? c-'0': c);
        i++;
    }
    E x = execute(i, operations);
    printf("%lld\n", x);
}