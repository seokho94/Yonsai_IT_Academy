package chapter6;

public class BoardExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Board board1 = new Board("����", "����");
		Board board2 = new Board("����", "����", "ȫ�浿");
		Board board3 = new Board("����", "����", "ȫ�浿", "2015-12-31");
		Board board4 = new Board("����", "����", "ȫ�浿", "2015-12-31", 5);
		System.out.println("**********Board1�� ����***********");
		System.out.println("Board1 ���� : " + board1.title + "\n" + "Board1 ���� : " + board1.content + "\n" + "Board1 �̸� : " + board1.writer + "\n" + "Board1 ��¥ : " + board1.date + "\n" + "Board1 ��ȸ�� : " + board1.hitcount + "\n");
		
		System.out.println("**********Board2�� ����***********");
		System.out.println("Board2 ���� : " + board2.title + "\n" + "Board2 ���� : " + board2.content + "\n" + "Board2 �̸� : " + board2.writer + "\n" + "Board2 ��¥ : " + board2.date + "\n" + "Board2 ��ȸ�� : " + board2.hitcount + "\n");
		
		System.out.println("**********Board3�� ����***********");
		System.out.println("Board3 ���� : " + board3.title + "\n" + "Board3 ���� : " + board3.content + "\n" + "Board3 �̸� : " + board3.writer + "\n" + "Board3 ��¥ : " + board3.date + "\n" + "Board3 ��ȸ�� : " + board3.hitcount + "\n");
		
		System.out.println("**********Board4�� ����***********");
		System.out.println("Board4 ���� : " + board4.title + "\n" + "Board4 ���� : " + board4.content + "\n" + "Board4 �̸� : " + board4.writer + "\n" + "Board4 ��¥ : " + board4.date + "\n" + "Board4 ��ȸ�� : " + board4.hitcount + "\n");	
	}

}