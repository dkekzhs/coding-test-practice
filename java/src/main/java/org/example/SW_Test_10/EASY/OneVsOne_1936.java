package org.example.SW_Test_10.EASY;

import java.util.Scanner;

public class OneVsOne_1936 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        if(A == 1 && B == 3){
            System.out.println("A");
        } else if (A==2 && B == 1) {
            System.out.println("A");
        }else if(A==3 && B == 2){
            System.out.println("A");
        }
        else{
            System.out.println("B");
        }
    }
}
