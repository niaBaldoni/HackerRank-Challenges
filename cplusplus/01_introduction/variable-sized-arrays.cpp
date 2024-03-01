#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
SAMPLE INPUT
2 2
3 1 5 4
5 1 2 8 9 3
0 1
1 3

2 2 means we have to read 4 total rows = 2 rows of data, and 2 rows with a question each
n = 2
q = 2

1 5 4 is our data for the first array, so we need an array of lenght 3
1 2 8 9 3 is our data for the second array, so we need an array of lenght 5

0 1 is our fist question = the number in position 1 in the 0th array
1 3 is instead asking the number in position 1 in the 3rd array
*/


int main() {
    // we can logically divide the algorithm into 2 main parts: data acquisition and data retrieval
    // we need to acquire n arrays
    // we need to answer q questions
    int n, q;
    cin >> n >> q;
    
    // data acquisition: we acquire n arrays by
    // - initialising a vector to store the n vectors
    // - initialising a new vector for each row, and acquiring the j numbers it's composed of
    
    int size, temp;
    vector<vector<int>> nvec;
    
    for (int i = 0; i < n; i++) {
        
        cin >> size;
        vector<int> ivec;
        
        for (int j = 0; j < size; j++) {
            cin >> temp;
            ivec.push_back(temp);
        }
        nvec.push_back(ivec);
    }
    
    // data retrieval: we answer the questions
    
    int arr, pos;
    for (int k = 0; k < q; k++) {
        cin >> arr >> pos;
        cout << nvec.at(arr).at(pos) << endl;
    }
    return 0;
}
