package chapter6;

public class CarFuelExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CarFuel myCar = new CarFuel();
		
		myCar.setGas(5);
		
		boolean gasState = myCar.isLeftGas();
		if(gasState) {
			System.out.println("����մϴ�.");
			myCar.run();
		}
		
		if(myCar.isLeftGas()) {
			System.out.println("gas�� ������ �ʿ䰡 �����ϴ�.");
		}
		else {
			System.out.println("gas�� �����ϼ���.");
		}
	}

}
