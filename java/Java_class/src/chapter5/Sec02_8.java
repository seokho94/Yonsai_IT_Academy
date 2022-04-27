package chapter5;

public class Sec02_8 {
	public static void main(String args[]) {
		int[] oldIntArray = {1,2,3};
		int[] newIntArray = new int[5];
		
		for(int i=0; i<oldIntArray.length; i++) {
			newIntArray[i] = oldIntArray[i];
		}
		
		for(int num : newIntArray) {
			System.out.print(num + ", ");
		}
	}
}
