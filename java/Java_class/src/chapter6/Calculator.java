package chapter6;

public class Calculator {
	void powerOn() {
		System.out.println("������ �մϴ�");		
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
		println("������ : " + result);
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
		System.out.println("�������� ���ϴ�.");
	}
}
