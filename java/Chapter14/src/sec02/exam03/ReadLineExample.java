package sec02.exam03;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.Reader;

public class ReadLineExample {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Reader reader = new FileReader(ReadLineExample.class.getResource("language.txt").getPath());
		
		BufferedReader br = new BufferedReader(reader);
		
		while(true) {
			String data = br.readLine();
			if(data == null) break;
			System.out.println(data);
		}
		
		br.close();
	}

}
