package chapter6;

public class MemberServiceExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MemberService mbs = new MemberService();
		boolean result = mbs.login("hong", "12345");
		if(result) {
			System.out.println("�α��� �Ǿ����ϴ�.");
			mbs.logout("hong");
		}
		else {
			System.out.println("id �Ǵ� password�� Ȯ�����ּ���.");
		}
		
	}

}
