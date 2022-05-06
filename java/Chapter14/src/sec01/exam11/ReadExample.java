package sec01.exam11;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;

public class ReadExample {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Reader rd = new FileReader("C:/Temp/tset7.txt");
		while(true) {
			int data = rd.read();
			if(data == -1 ) break;
			System.out.println((char)data);
		}
		rd.close();
	}

}
