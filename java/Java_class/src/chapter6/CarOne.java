package chapter6;

public class CarOne {
	int speed;
	
	void run() {
		System.out.println(speed + "���� �޸��ϴ�.");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CarOne myCar = new CarOne();
		myCar.speed = 60;
		myCar.run();
	}

}
