package org.example.코드업기초100제;

import java.util.Scanner;
public class SugarCookiePicking_1098 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sizeX = sc.nextInt();
        int sizeY = sc.nextInt();
        int[][] a = new int[sizeX][sizeY];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                a[i][j] = 0;
            }
        }
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int l = sc.nextInt();
            int dir = sc.nextInt();
            int x = sc.nextInt() -1;
            int y = sc.nextInt() -1;

            if(dir == 0){
                if(x+l> a[0].length){
                    continue;
                }
                for (int j = x; j < x+l; j++) {
                    a[x][j] = 1;
                }
            }
            else{
                if (x + l > a.length) {
                    continue;
                }
                for (int j = x; j < x+l ; j++) {
                    a[j][y] = 1;
                }
            }

        }
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j]+" ");
            }
            System.out.println();
        }
    }
}
