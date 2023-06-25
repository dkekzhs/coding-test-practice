package org.example.코드업기초100제;

import java.util.Scanner;

public class FlipTheBall_1097 {
    public static void main(String[] args) {
        int[][] b = new int[19][19];
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                b[i][j] = sc.nextInt();
            }
        }

        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int x = sc.nextInt() - 1;
            int y = sc.nextInt() - 1 ;
            for (int j = 0; j <19 ; j++) {
                if(b[x][j] == 0 ) b[x][j] = 1;
                else b[x][j] = 0;
            }
            for (int j = 0; j < 19; j++) {
                if(b[j][y] == 0) b[j][y] = 1;
                else b[j][y] = 0;
            }
        }
        for (int i = 0; i < b.length; i++) {
            for (int j = 0; j < b[i].length; j++) {
                System.out.print(b[i][j] + " ");
            }
            System.out.println();
        }

    }
}
