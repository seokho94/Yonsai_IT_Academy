package sec01.exam10;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

public class WriteExample {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Writer wr = new FileWriter("C:/Temp/test8.txt");
		
		String str = "ABC";
		
		wr.write(str);
		
		wr.flush();
		wr.close();
	}

}
