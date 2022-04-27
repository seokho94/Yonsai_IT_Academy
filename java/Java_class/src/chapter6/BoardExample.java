package chapter6;

public class BoardExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Board board1 = new Board("제목", "내용");
		Board board2 = new Board("제목", "내용", "홍길동");
		Board board3 = new Board("제목", "내용", "홍길동", "2015-12-31");
		Board board4 = new Board("제목", "내용", "홍길동", "2015-12-31", 5);
		System.out.println("**********Board1의 정도***********");
		System.out.println("Board1 제목 : " + board1.title + "\n" + "Board1 내용 : " + board1.content + "\n" + "Board1 이름 : " + board1.writer + "\n" + "Board1 날짜 : " + board1.date + "\n" + "Board1 조회수 : " + board1.hitcount + "\n");
		
		System.out.println("**********Board2의 정도***********");
		System.out.println("Board2 제목 : " + board2.title + "\n" + "Board2 내용 : " + board2.content + "\n" + "Board2 이름 : " + board2.writer + "\n" + "Board2 날짜 : " + board2.date + "\n" + "Board2 조회수 : " + board2.hitcount + "\n");
		
		System.out.println("**********Board3의 정도***********");
		System.out.println("Board3 제목 : " + board3.title + "\n" + "Board3 내용 : " + board3.content + "\n" + "Board3 이름 : " + board3.writer + "\n" + "Board3 날짜 : " + board3.date + "\n" + "Board3 조회수 : " + board3.hitcount + "\n");
		
		System.out.println("**********Board4의 정도***********");
		System.out.println("Board4 제목 : " + board4.title + "\n" + "Board4 내용 : " + board4.content + "\n" + "Board4 이름 : " + board4.writer + "\n" + "Board4 날짜 : " + board4.date + "\n" + "Board4 조회수 : " + board4.hitcount + "\n");	
	}

}