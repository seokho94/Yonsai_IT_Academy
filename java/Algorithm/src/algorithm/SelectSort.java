package algorithm;

import java.util.Random;

public class SelectSort {
	public static void main(String args[]) {
		Random rand = new Random();
		int arr[] = new int[10];
		for(int i=0; i<arr.length; i++) {
			arr[i] = (rand.nextInt(10)+1);
		}
		System.out.println("선택 정렬");
		for(int num : arr) {
			System.out.print("[" + num + "]" + " ");
		}
		System.out.println("\n");
		int idx = 0;
		while(idx<arr.length) {
			int min = 12;
			int change_idx = 0;
			for(int i=idx; i<arr.length; i++) {
				if(min > arr[i]) {
					min = arr[i];
					change_idx = i;					
				} 
			}
			int temp = arr[change_idx];
			arr[change_idx] = arr[idx];
			arr[idx] = temp;
			idx++;
			for(int num : arr) {
				System.out.print("["+num+"]");
			}
			System.out.println("------>"+idx+"번 pass 결과");
			if(chackArr(arr)) {
				break;
			}
		}
 	}
	public static boolean chackArr(int arr[]) {
		boolean sign = false;
		for(int i=0; i<arr.length-1; i++) {
			if(arr[i]<=arr[i+1]) {
				sign = true;
			}
			else {
				sign = false;
				break;
			}
		}
		return sign;
	}
}
