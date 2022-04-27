package chapter5;

public class Sec02_9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] oldStrArray = {"java", "array", "copy"};
		String[] newStrArray = new String[5];
		
		System.arraycopy(oldStrArray, 0, newStrArray, 0, oldStrArray.length);
		
		for(String txt : newStrArray) {
			System.out.print(txt + ", ");
		}
	}

}
