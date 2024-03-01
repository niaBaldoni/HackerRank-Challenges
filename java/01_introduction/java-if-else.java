/*
This code evaluates an integer in input.
If the number is odd, or is even but in the inclusive range of 6 to 20, then it's a Weird number.
Otherwise, it's Not Weird.
*/


import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();
        
        if(N%2==1 || (N%2==0 && 6<=N && N<=20)){
            System.out.println("Weird");
        } else {
            System.out.println("Not Weird");
        }
    }
}
