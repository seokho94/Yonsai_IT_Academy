package constructor;

public class PersonTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Person personKim = new Person();
		  personKim.name = "김유신";
		  personKim.weight = 85.5F;
		  personKim.height = 180.0F;
		  System.out.println("personKim name : " + personKim.name + "personKim weight : " + personKim.weight + "personKim height : " + personKim.height);
		  
		  Person personLee = new Person("이순신", 175, 75);
		  System.out.println("personLee name : " + personLee.name + "personLee weight : " + personLee.weight + "personLee height : " + personLee.height);
	}

}
