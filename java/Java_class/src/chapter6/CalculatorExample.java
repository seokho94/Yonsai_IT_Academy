package chapter6;

public class CalculatorExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Calculator myCal = new Calculator();
		myCal.powerOn();
		
		int result1 = myCal.plus(5, 6);
		System.out.println("result1 : " + result1);
		
		byte x = 10;
		byte y = 4;
		double result2 = myCal.divide(x, y);
		System.out.println("result2 : " + result2);
		
		double result3 = myCal.areaRectangle(10);
		double result4 = myCal.areaRectangle(10, 20);
		
		System.out.println("정사각형의 넓이 = " + result3);
		System.out.println("직사각형의 넓이 = " + result4);
		
		myCal.excute();
		
		myCal.powerOff();
	}

}
