package org.example.코드업기초100제;

import java.sql.Array;
import java.util.ArrayList;
import java.util.Scanner;


public class AttendanceCheck_1093 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i <T ; i++) {
            list.add(sc.nextInt());
        }
        Integer [] a = new Integer[23];
        for (int i = 0; i < 23; i++) {
            a[i] = 0;
        }
        for (int i = 0; i < list.size(); i++) {
            a[list.get(i)-1] += 1;
        }
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i]+" ");
        }
    }
}
