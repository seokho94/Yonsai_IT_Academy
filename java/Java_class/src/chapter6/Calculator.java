package chapter6;

public class Calculator {
	void powerOn() {
		System.out.println("전원을 켭니다");		
	}
	
	int plus(int x, int y) {
		int result = x+y;
		return result;
	}
	
	double divide(int x, int y) {
		double result = (double)x / (double)y;
		return result;
	}
	
	double avg(int x, int y) {
		double sum = plus(x, y);
		double result = sum /2;
		return result;
	}
	
	void excute() {
		double result = avg(7, 10);
		println("실행결과 : " + result);
	}
	
	void println(String message) {
		System.out.println(message);
	}
	
	double areaRectangle(double width) {
		return width * width;
	}
	
	double areaRectangle(double width, double height) {
		return width * height;
	}
	
	void powerOff() {
		System.out.println("전원응ㄹ 끕니다.");
	}
}
