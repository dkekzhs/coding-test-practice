package org.example.SW_Test_10.MIDDLE;

import java.util.Scanner;

public class RotateNum_1961 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T ; test_case++) {
            int N = sc.nextInt();
            int[][] map = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    map[i][j] = sc.nextInt();
                }
            }
            String[] one = new String[N];
            String[] two = new String[N];
            String[] three = new String[N];
            for (int i = 0; i < N; i++) {
                String temp = "";
                for (int j = N-1 ; j >=0; j--) {
                    temp += String.valueOf(map[j][i]);
                }
                one[i] = temp;
            }
            for (int i = N-1; i >=0 ; i--) {
                String temp2 = "";
                for (int j = N-1; j >=0 ; j--) {
                    temp2 += String.valueOf(map[i][j]);
                }
                two[N - 1 - i] = temp2;
            }
            for (int i = N-1; i >= 0; i--) {
                String temp3 = "";
                for (int j = 0; j < N; j++) {
                    temp3 += String.valueOf(map[j][i]);
                }
                three[N - 1 - i] = temp3;
            }
            System.out.println("#" + test_case);
            for (int i = 0; i < N; i++) {
                System.out.print(one[i]+ " "+ two[i]+" "+three[i]);
                System.out.println();
            }
        }
        
    }
}
