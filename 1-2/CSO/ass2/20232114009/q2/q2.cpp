#include <stdio.h>
#include <iostream>
#define E long long

// #pragma once

#include <chrono> // for std::chrono functions

class Timer
{
private:
    // Type aliases to make accessing nested type easier
    using Clock = std::chrono::steady_clock;
    using Second = std::chrono::duration<double, std::ratio<1> >;

    std::chrono::time_point<Clock> m_beg{ Clock::now() };

public:
    void reset()
    {
        m_beg = Clock::now();
    }

    double elapsed() const
    {
        return std::chrono::duration_cast<Second>(Clock::now() - m_beg).count();
    }
};

extern "C" E choose(E n, E r);
// {
//     if (r == 0) {
//         return 1;
//     }
//     E d = n-r;
//     if (d < r) {
//         r = d;
//     }
//     E ans = n;
//     ans *= choose(n-1, r-1);
//     ans /= r;
//     return ans;
// }

E choose2(E n, E r) {
    if (n-r < r) r = n-r;
    E ans = 1;
    for (E i = 1; i <= r; ++i) {
        ans *= n-r+i;
        ans /= i;
    }
    return ans;
}

int main() {
    E n, r;
    scanf("%lld%lld", &n, &r);

    Timer t;
    choose(n, r);
    std::cout << "recursive: " << choose(n, r) << ' ' << t.elapsed() << '\n';

    t.reset();
    choose2(n, r);
    std::cout << "iterative: " << choose2(n, r) << ' ' << t.elapsed() << '\n';
    return 0;
}