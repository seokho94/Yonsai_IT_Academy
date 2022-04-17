public class step1 {
	
	public static void main(String[] args) {
		System.out.println("Hello, World!");
		textPrint("Heeeeeeeeello, World!");
		int result = sumNum(4,5);
		textPrint(String.valueOf(result));
		System.out.println("°¡³ª´Ù");
	}
	
	public static void textPrint(String str) {
		System.out.println(str);
	}
	
	 static int sumNum(int a, int b) {
		int result = a + b;
		return result;
	}
}