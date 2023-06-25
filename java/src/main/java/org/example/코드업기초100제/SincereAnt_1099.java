package org.example.코드업기초100제;

import java.util.Scanner;
public class SincereAnt_1099 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = 1; int y = 1;
        int[][] map = new int[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                map[i][j] = sc.nextInt();
            }
        }
        int[][] solutuon = solutuon(x, y, map);
        for (int i = 0; i < solutuon.length; i++) {
            for (int j = 0; j < solutuon[i].length; j++) {
                System.out.print(solutuon[i][j]+" ");
            }
            System.out.println();
        }
    }

    public static int[][] solutuon(int w, int h, int[][] map) {
        while(map[h][w] != 2){
            map[h][w] = 9;
            if(map[h][w+1] != 1) w += 1;
            else if (map[h+1][w] != 1) h += 1;
            else break;
        }
        map[h][w] = 9;
        return map;
    }
}
