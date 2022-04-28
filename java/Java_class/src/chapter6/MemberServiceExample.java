package chapter6;

public class MemberServiceExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MemberService mbs = new MemberService();
		boolean result = mbs.login("hong", "12345");
		if(result) {
			System.out.println("로그인 되었습니다.");
			mbs.logout("hong");
		}
		else {
			System.out.println("id 또는 password를 확인해주세요.");
		}
		
	}

}
