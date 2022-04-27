package chapter5;

public class Sec02_11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int max = 0;
		int[] array = {1, 5, 3, 8 ,2};
		
		for(int num : array) {
			if(num > max) max = num;
		}
		
		System.out.println("max : " + max);
	}

}
