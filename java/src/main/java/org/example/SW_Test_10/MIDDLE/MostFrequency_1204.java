package org.example.SW_Test_10.MIDDLE;


import java.io.*;
import java.util.StringTokenizer;

public class MostFrequency_1204 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] stu = new int[101];
            for (int i = 0; i < 1000; i++) {
                stu[Integer.parseInt(st.nextToken())] += 1;
            }
            int max = 0;
            int idx = 0;
            for (int i = 100; i >= 0; i--) {
                if(stu[i] > max){
                    max = stu[i];
                    idx = i;
                }
            }
            bw.append("#" + test_case + " " + idx+"\n");
            bw.flush();
        }
        bw.close();
    }
}
