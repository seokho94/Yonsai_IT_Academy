package lotto;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		selectNum lotto = new selectNum();
		Scanner sc = new Scanner(System.in);
		int count = sc.nextInt();
		System.out.println(count + "°³ ·Î¶Ç : ");
		lotto.setNum(count);
	}

}