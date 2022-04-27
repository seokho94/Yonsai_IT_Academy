package chapter6;

public class MemberExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Member member = new Member();
		member.name = "최하얀";
		member.age = 23;
		member.id = "white00";
		member.password = "gkdis123";
		
		System.out.println("이름 : " + member.name);
		System.out.println("나이 : " + member.age);
		System.out.println("아이디 : " + member.id);
		System.out.println("패스워드 : " + member.password);
	}

}
