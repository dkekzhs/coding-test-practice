package org.example.SW_Test_10.EASY;

import java.util.Scanner;
public class AddDigits_2058 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 0;
        int i = sc.nextInt();
        String s = String.valueOf(i);
        char[] chars = s.toCharArray();
        for (int j = 0; j < chars.length; j++) {
            a += Integer.parseInt(String.valueOf(chars[j]));

        }
        System.out.println(a);
    }
}
