package chapter6;

public class CarSpeedExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CarSpeed cs = new CarSpeed();
		
		cs.keyTurnOn();
		cs.run();
		int speed = cs.getSpeed();
		System.out.println("���� �ӵ� : " + speed + "km/h");
	}

}
