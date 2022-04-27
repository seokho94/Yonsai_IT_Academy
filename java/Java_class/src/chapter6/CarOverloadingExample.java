package chapter6;

public class CarOverloadingExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CarOverloading car1 = new CarOverloading();
		CarOverloading car2 = new CarOverloading("그랜저");
		CarOverloading car3 = new CarOverloading("그랜저", "black");
		CarOverloading car4 = new CarOverloading("그랜저", "black", 280);
		System.out.println("---------Car1-----------");
		System.out.println("car1 companny : " +car1.company + "\n" + "car1 model : " + car1.model + "\n" + "car1 color : " + car1.color + "\n" + "car1 maxSpeed : " + car1.maxSpeed + "\n");
		
		System.out.println("---------Car2-----------");
		System.out.println("car2 companny : " +car2.company + "\n" + "car2 model : " + car2.model + "\n" + "car2 color : " + car2.color + "\n" + "car2 maxSpeed : " + car2.maxSpeed + "\n");
		
		System.out.println("---------Car3-----------");
		System.out.println("car3 companny : " +car3.company + "\n" + "car3 model : " + car3.model + "\n" + "car3 color : " + car3.color + "\n" + "car3 maxSpeed : " + car3.maxSpeed + "\n");
		
		System.out.println("---------Car4-----------");
		System.out.println("car4 companny : " +car4.company + "\n" + "car4 model : " + car4.model + "\n" + "car4 color : " + car4.color + "\n" + "car4 maxSpeed : " + car4.maxSpeed + "\n");
	}
}
