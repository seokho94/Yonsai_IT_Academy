package alice;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Student std1 = new Student();
		std1.studentID = 123;
		std1.studentName = "±è±è±è";
		std1.grade = 96;
		std1.address ="Korea";
		System.out.println("StudentID : "+std1.studentID +"\n" +"StudentName : "+ std1.studentName +"\n" + "Grade : "+ std1.grade +"\n"+ "Address : "+ std1.address);
		
		System.out.println("----------------------------------------------");
		
		Student studentAhn = new Student();
		studentAhn.studentName = "¾È¿¬¼ö";
		System.out.println(studentAhn.studentName);
		System.out.println(studentAhn.getStudentName());
	}
}