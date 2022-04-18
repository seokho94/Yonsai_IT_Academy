package lotto;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Random;

public class selectNum {
	public void setNum(int num) {
		HashSet<Integer> lotto = new HashSet<Integer>();
		Random rnd = new Random();
		int count = 0;
		while(count < num) {
			lotto.add((rnd.nextInt(45)+1));
			if(lotto.size()==6) {
				printNum(lotto);
				lotto.clear();
				count++;
			}
		}
	}
	
	public void printNum(HashSet lotto) {
		List<Integer> sortedNum = new ArrayList<>(lotto);
		Collections.sort(sortedNum);
		for(Integer data : sortedNum) {
			System.out.print(data + " ");
		}
		System.out.println();
	}
}
