package org.example.SW_Test_10.MIDDLE;

import java.util.*;
public class Sudoku_1974 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int N = 9;
        for (int test_case = 1; test_case <= T; test_case++) {
            int[][] Map = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    Map[i][j] = sc.nextInt();
                }
            }

            int low = Low(Map, N);
            int col = Col(Map, N);
            int box = Box(Map, N);
            if(low ==9 && col == 9 && box == 9){

                System.out.println("#"+test_case+" "+1);
            }
            else{
                System.out.println("#"+test_case+" "+0);
            }
        }
    }
    private  static  int Count(List<Integer> data){
        int[] real = new int[10];
        real[0] = 1;
        for (int i = 0; i < data.size(); i++) {
            real[data.get(i)] += 1;
        }
        for (int i = 0; i < real.length; i++) {
            if(real[i] <0 |real[i] >=2){
                return 0;
            }
        }
        return 1;
    }
    private static int Box(int[][] map, int n) {
        int count = 0;
        for (int i = 0; i <n ; i+=3) {
            for (int j = 0; j <n ; j+=3) {
                List<Integer> c = new ArrayList<>();
                c = Check(i, j, map,c);
                count += Count(c);
            }
        }
        return count;
    }

    private static List<Integer> Check(int i, int j, int[][] map, List<Integer> c) {
        for (int k = j; k < j+3; k++) {
            for (int l = i; l < i+3; l++) {
                c.add(map[k][l]);
            }
        }
        return c;
    }

    private static int Low(int[][] map, int n) {
        int answer = 0;
        for (int i = 0; i <n; i++) {
            List<Integer> a = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                a.add(map[i][j]);
            }
            answer +=Count(a);
        }
        return answer;
    }

    private static int Col(int[][] map, int n) {
        int answer2 = 0;
        for (int i = 0; i <n; i++) {
            List<Integer> b = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                b.add(map[j][i]);
            }
            answer2 += Count(b);
        }
        return answer2;
    }
}
