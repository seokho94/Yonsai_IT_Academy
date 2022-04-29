package chapter7;

public class ComputerExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int r = 10;
		Calculator calculator = new Calculator();
		System.out.println("원면적 : " + calculator.areaCircle(r)+"\n");
		Computer computer = new Computer();
		System.out.println("원멱적 : " + computer.areaCircle(r));
	}

}
