#include <iostream>
#include <cstdio>
using namespace std;

// the exercise requires to create the function max_of_four(int a, int b, int c, int d)
// since we don't need to order (we only need the max value overall),
// and since the comparison is between 4 integers (no more, no less),
// we can use the divide et impera technique to divide the problem into 2 subproblems which are easy to resolve
// What is the max between a, b, c and d? Well, it will be the max number between x and y
// where x is the max between a and b, and y is the max between c and d

int max_of_two(int x, int y) {
    if (x > y) {
        return x;
    } else {
        return y;
    }
}

int max_of_four(int a, int b, int c, int d) {
    return max_of_two(max_of_two(a, b), max_of_two(c,d));
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
