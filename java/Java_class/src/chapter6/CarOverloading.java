package chapter6;

public class CarOverloading {
	String company = "현대자동차";
	String model;
	String color;
	int maxSpeed;
	
	CarOverloading(){
//		this.model = "그랜저";
//		this.color = "Green";
//		this.maxSpeed = 240;
		this("그랜저", "Green", 240);
	}
	
	CarOverloading(String model){
//		this.model = model;
//		this.color = "red";
//		this.maxSpeed = 250;
		this(model, "red", 250);
	}
	
	CarOverloading(String model, String color){
//		this.model = model;
//		this.color = color;
//		this.maxSpeed = 260;
		this(model, color, 260);
	}
	
	CarOverloading(String model, String color, int maxSpeed){
//		this.model = model;
//		this.color = color;
//		this.maxSpeed = maxSpeed;
		this.model = model;
		this.color = color;
		this.maxSpeed = maxSpeed;
	}
	
}
