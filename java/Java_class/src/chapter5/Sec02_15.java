package chapter5;

public class Sec02_15 {
	public static void main(String[] args) {
		LoginResult result = LoginResult.FAIL_PASSWORD;
		if(result == LoginResult.SUCCESS) {
			System.out.println("로그인에 성공하셨습니다.");
		}
		else if(result == LoginResult.FAIL_ID) {
			System.out.println("아이디가 잘못되었습니다.");
		}
		else if(result == LoginResult.FAIL_PASSWORD) {
			System.out.println("패스워드를 확인해주세요");
		}
	}
}