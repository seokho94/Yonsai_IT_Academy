package algorithm;

import java.util.Random;

public class InsertionSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random rand = new Random();
		int arr[] = new int[10];
		for(int i=0; i<arr.length; i++) {
			arr[i] = (rand.nextInt(10)+1);
		}
		System.out.println("삽입 정렬");
		for(int num : arr) {
			System.out.print("[" + num + "]" + " ");
		}
		System.out.println("\n");
		int idx = 1;
		while(idx<arr.length) {
			int selectNum = arr[idx];
			for(int i = idx-11; i>0; i--) {
				if(selectNum<arr[i]) {
					int temp = arr[i-1];
					arr[i-1] = selectNum;
					arr[i] = temp;
				}
			}
			if((idx-1)==0) {
				if(arr[idx]<arr[0]) {
					arr[idx] = arr[0];
					arr[0] = selectNum;
				}
			}
			idx++;
//			for(int num : arr) {
//				System.out.print("["+num+"]");
//			}
//			System.out.println("------>"+(idx-1)+"번 pass 결과");
//			if(chackArr(arr)) {
//				break;
//			}
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
