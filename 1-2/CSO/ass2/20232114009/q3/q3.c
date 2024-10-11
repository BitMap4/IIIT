#include <stdio.h>
typedef long long E;

extern E calculate(E n, E expr[]);
// {
//     stack<E> s;
//     for(int i=0; i<n; i++) {
//         case (expr[i]) {
//             case '+': {
//                 E a = s.top();
//                 s.pop();
//                 E b = s.top();
//                 s.pop();
//                 s.push(a+b);
//                 break;
//             }
//             case '-': {
//                 E a = s.top();
//                 s.pop();
//                 E b = s.top();
//                 s.pop();
//                 s.push(a-b);
//                 break;
//             }
//             case '*': {
//                 E a = s.top();
//                 s.pop();
//                 E b = s.top();
//                 s.pop();
//                 s.push(a*b);
//                 break;
//             }
//             case '/': {
//                 E a = s.top();
//                 s.pop();
//                 E b = s.top();
//                 s.pop();
//                 s.push(a/b);
//                 break;
//             }
//             default: {
//                 s.push(expr[i]);
//             }
//         }
//     }
// }

int main() {
    E n;
    scanf("%lld", &n);
    scanf("%*c");
    E expr[1+n/2];  
    int i=0;
    char c;
    while (scanf("%c", &c)) {
        if (c == '\n') break;
        if (c == ' ') continue;
        expr[i] = (E) ((c<='9' && c>='0') ? c-'0': c);
        i++;
    }
    E x = calculate(i, expr);
    printf("%lld\n", x);
}