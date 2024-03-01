#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // reusing the string list I created for the previous exercise
    string lit[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    //acquiring input values
    int a, b;
    cin >> a;
    cin >> b;
    
    for (int i = a; i <= b; i++) {
        // if 1 <= i <= 9 I grab the str value
        if (1 <= i && i <= 9) {
            cout << lit[i-1] << endl;
        
        // else, I calculate if odd or even
        } else if (i > 9) {
            if (i%2 == 0) {
                cout << "even" << endl;
            } else {
                cout << "odd" << endl;
            }
        }
    }
    
    return 0;
}
