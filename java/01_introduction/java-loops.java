/*

1 series - a,b,n

(a + (2^0)*b), (a + (2^0)*b) + (2^1)*b), ... , (a + (2^0)*b + (2^1)*b + ... + (2^n-1)*b)

for j in range(0, n):
    ris += (2^j)*b
    print(ris)

*/

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i=0; i<t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int ris = a;
            for(int j=0; j<n; j++){
                ris = ris + (int)Math.pow(2,j)*b;
                System.out.printf("%d ", ris);
            }
            System.out.printf("%n");
        }
        in.close();
    }
}