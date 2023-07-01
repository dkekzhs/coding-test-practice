package org.example.SW_Test_10.MIDDLE;

import java.util.Scanner;

public class CatchFly_12712 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[][] map = new int[N][N];
            for (int i = 0; i < map.length; i++) {
                for (int j = 0; j < map[i].length; j++) {
                    map[i][j] = sc.nextInt();
                }
            }
            int[] dw = {-1, 1, 0, 0};
            int[] dh = {0, 0, -1, 1};
            int[] dww = {-1, 1, -1, 1};
            int[] dhh = {-1, 1, 1, -1};
            int answer = 0;
            for (int i = 0; i < map.length; i++) {
                for (int j = 0; j < map[i].length; j++) {
                    int temp = map[i][j];
                    int temp2 = map[i][j];

                    for (int k = 0; k < 4; k++) {
                        for (int l = 1; l <M; l++) {
                            int tempDw = j + dw[k] * l;
                            int tempDh = i + dh[k] * l;
                            int tempDww = j+ dww[k] * l;
                            int tempDhh = i+ dhh[k] * l;
                            if ((-1 <tempDw && tempDw < N )&& (-1 < tempDh && tempDh < N)) {
                                temp += map[tempDh][tempDw];
                            }
                            if ((-1 < tempDww && tempDww <N)  && (-1 < tempDhh && tempDhh < N)) {
                                temp2 += map[tempDhh][tempDww];
                            }
                        }
                    }
                    int total = Math.max(temp, temp2);
                    if(answer < total){
                        answer = total;
                    }
                }
            }
            System.out.println("#"+test_case+" " + answer);
        }

    }
}
