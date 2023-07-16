package org.example.SW_Test_10.HIGH;

import java.awt.*;
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class SupplyRoute_1249 {
    static int[][] Map, TempList;
    static int T,N;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            N = Integer.parseInt(br.readLine());
            Map = new int[N][N];
            TempList = new int[N][N];
            for (int i = 0; i < N; i++) {
                String[] split = br.readLine().split("");
                for (int j = 0; j < N; j++) {
                    Map[i][j] = Integer.parseInt(split[j]);
                }
            }
            int answer = bfs(0, 0);
            bw.append("#"+test_case+" "+answer+"\n");
            bw.flush();
        }
        bw.close();
        br.close();
    }

    private static int bfs(int x, int y) {
        for (int i = 0; i <N; i++) {
            for (int j = 0; j < N; j++) {
                TempList[i][j] = Integer.MAX_VALUE;
            }
            TempList[0][0] = 0;
        }
        Queue<Point> que = new LinkedList<>();
        que.add(new Point(x, y));
        while(!que.isEmpty()){
            Point p = que.poll();
            int xx = p.x;
            int yy = p.y;

            for (int i = 0; i < 4; i++) {
                int xxx = xx + dx[i];
                int yyy = yy + dy[i];
                if(0> xxx || xxx >= N)continue;
                if(0> yyy || yyy >= N)continue;

                if (TempList[xx][yy] + Map[xxx][yyy] < TempList[xxx][yyy]) {
                    TempList[xxx][yyy] = TempList[xx][yy] + Map[xxx][yyy];
                    que.add(new Point(xxx, yyy));
                }
            }
        }
        return TempList[N - 1][N - 1];
    }
}
