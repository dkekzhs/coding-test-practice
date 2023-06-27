package org.example.SW_Test_10.EASY;

import java.util.Arrays;
import java.util.Scanner;

public class midIndex_2063 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] arrays = new int[T];
        for (int j = 0; j < arrays.length ; j++) {
            arrays[j] = sc.nextInt();
        }
        int[] ints = Arrays.stream(arrays).sorted().toArray();
        System.out.println(ints[T/2]);

    }
}
