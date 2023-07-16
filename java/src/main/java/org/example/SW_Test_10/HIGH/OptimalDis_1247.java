package org.example.SW_Test_10.HIGH;

import java.awt.*;
import java.io.*;
import java.util.StringTokenizer;

public class OptimalDis_1247 {
    static Point home, comp;
    static Point[] cust;
    static int min, N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            N = Integer.parseInt(br.readLine());
            min = Integer.MAX_VALUE;
            StringTokenizer st = new StringTokenizer(br.readLine());
            home = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            comp = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            cust = new Point[N];
            for (int i = 0; i < N ; i++) {
                cust[i] = new Point(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
            }
            calcul(0,new Point[N],new boolean[N],0);
            bw.write("#"+test_case+" "+min+"\n");
            bw.flush();
        }
        bw.close();

    }

    private static void calcul(int cnt, Point[] data, boolean[] visited, int dis) {
        if(dis > min){
            return;
        }
        if(cnt == N){
            int answer = dis + distance(comp.x, data[N-1].x, comp.y, data[N-1].y);
            min = Math.min(answer, min);
            return;
        }
        for (int i = 0; i < N; i++) {
            if(visited[i]) continue;
            visited[i] = true;
            data[cnt] = cust[i];
            if(cnt == 0){
                calcul(cnt+1,data,visited,dis+distance(home.x,data[cnt].x,home.y,data[cnt].y));
            }
            else{
                calcul(cnt+1,data,visited,dis+distance(data[cnt-1].x,data[cnt].x,data[cnt-1].y,data[cnt].y));
            }
            visited[i] = false;
        }
    }

    static int distance(int x, int x1, int y, int y2) {

    return Math.abs(x - x1) + Math.abs(y - y2);

    }
}
