import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BufferTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		try {
			String[] inputData = br.readLine().split("");
			br.close();
			for(String str : inputData) {
				bw.write(str+"\n");
			}
			bw.flush();
			bw.close();
		}
		catch(Exception e) {
			
		}
	}

}
