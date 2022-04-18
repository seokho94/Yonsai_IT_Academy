package hiding;

public class MyDateTest {
	public static void main(String args[]) {
		MyDate date = new MyDate();
		date.month = 2;
		date.day = 31;
		date.year = 2016;
		System.out.println("Month : " + date.month + "Day : "+date.day + "Year : " + date.year);
	}
}
