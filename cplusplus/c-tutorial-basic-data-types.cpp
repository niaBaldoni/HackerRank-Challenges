#include <iostream>
#include <cstdio>
using namespace std;

// Int ("%d"): 32 Bit integer
// Long ("%ld"): 64 bit integer
// Char ("%c"): Character type
// Float ("%f"): 32 bit real value
// Double ("%lf"): 64 bit real value

int main() {
    int vint;
    long vlong;
    char vchar;
    float vfloat;
    double vdouble;
    
    // the additional arguments for scanf are expected to be pointers
    scanf("%d %ld %c %f %lf", &vint, &vlong, &vchar, &vfloat, &vdouble);
    
    printf("%d\n", vint);
    printf("%ld\n", vlong);
    printf("%c\n", vchar);
    printf("%.3f\n", vfloat);
    printf("%.9lf\n", vdouble);
    return 0;
}
