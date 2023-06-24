package org.example.코드업기초100제;

import java.util.Scanner;

public class ListOfNumbers_1089 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int degree = sc.nextInt();
        int Index = sc.nextInt();

        System.out.println((degree*(Index-1)) + start);
    }
}