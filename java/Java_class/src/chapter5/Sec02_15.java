package chapter5;

public class Sec02_15 {
	public static void main(String[] args) {
		LoginResult result = LoginResult.FAIL_PASSWORD;
		if(result == LoginResult.SUCCESS) {
			System.out.println("�α��ο� �����ϼ̽��ϴ�.");
		}
		else if(result == LoginResult.FAIL_ID) {
			System.out.println("���̵� �߸��Ǿ����ϴ�.");
		}
		else if(result == LoginResult.FAIL_PASSWORD) {
			System.out.println("�н����带 Ȯ�����ּ���");
		}
	}
}