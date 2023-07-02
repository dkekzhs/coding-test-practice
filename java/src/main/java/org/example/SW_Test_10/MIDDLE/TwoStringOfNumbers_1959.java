package org.example.SW_Test_10.MIDDLE;

import java.util.Scanner;

public class TwoStringOfNumbers_1959 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int z = 0;
            int[] one = new int[N];
            int[] two = new int[M];
            for (int i = 0; i < N; i++) {
                one[i] = sc.nextInt();
            }
            for (int i = 0; i < M; i++) {
                two[i] = sc.nextInt();
            }
            if (one.length > two.length) {
                int[] tempList = one;
                int tempN = N;
                N = M;
                M = tempN;
                one = two;
                two = tempList;
            }
            int answer = 0;
            int j;
            while(z+N < M +1){
                int temp = 0;
                j = 0;
                for (int i = z; i < z+N; i++) {
                    temp += one[j] * two[i];
                    j += 1;

                }
                z += 1;
                if( temp> answer) answer = temp;

            }
            System.out.println("#" + test_case+" "+answer);

        }
    }
}
