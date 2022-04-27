package chapter6;

public class CarAttributionExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CarAttribution carat = new CarAttribution("black", 42122, "12가1234");
		System.out.println("색상 : " + carat.color);
		System.out.println("시리얼넘버 : " + carat.cc);
		System.out.println("차량번호 : " + carat.number);
	}

}
