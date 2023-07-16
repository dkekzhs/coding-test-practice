package org.example.SW_Test_10.HIGH;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class ChangTown_7465 {
    static ArrayList<Integer>[] map;
    static int N,M,a,b;
    static boolean [] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <=T ; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            map = new ArrayList[N + 1];
            visited = new boolean[N + 1];
            for (int i = 0; i < map.length; i++) {
                map[i] = new ArrayList<Integer>();
            }
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                map[a].add(b);
                map[b].add(a);
            }
            int answer = 0;
            visited[0] = true;
            for (int i = 0; i <=N; i++) {
                if(visited[i] == true) continue;
                dfs(i);
                answer += 1;

            }
            bw.append("#" + test_case + " " + answer+"\n");
            bw.flush();
        }
        bw.close();
        br.close();
    }

    private static void dfs(int idx) {
        visited[idx] = true;
        for (int next : map[idx]) {
            if(visited[next]) continue;
            dfs(next);
        }
    }
}
