package chapter6;

public class CarOne {
	int speed;
	
	void run() {
		System.out.println(speed + "으로 달립니다.");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CarOne myCar = new CarOne();
		myCar.speed = 60;
		myCar.run();
	}

}
