
#include <stdio.h>
#include <inttypes.h>

#include "day1.h"

int main() {
    uint_fast16_t inc1 = 0, inc2 = 0;
    size_t N = sizeof(xs) / sizeof(uint_fast16_t);
    for (uint_fast16_t i = 1; i < N; inc1 += xs[i++] < xs[i])
        ;  // illegal, but very funny

    uint16_t new, last = xs[0] + xs[1] + xs[2];
    for (uint_fast16_t i = 3; i < N; i++) {
        new = last - xs[i - 3] + xs[i];
        inc2 += last < new;
        last = new;
    }

    printf("inc1: %"PRIuFAST16", inc2: %"PRIuFAST16"\n", inc1, inc2);




    return 0;
}