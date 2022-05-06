package sec01.exam08;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

public class WriteExample {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Writer writer = new FileWriter("C:/Temp/test8.txt");
		
		char[] array = {'A', 'B', 'C'};
		
		writer.write(array);
		
		writer.flush();
		writer.close();
	}

}
