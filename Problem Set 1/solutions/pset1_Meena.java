import java.util.*;

public class pset1_Meena{
	public static void main(String [] args) {
		System.out.println(findAnswer());
	}

	// takes in input
	// finds the maximum no of postings in for each line in input
	// concatenates answers
	static String findAnswer() {
		Scanner sc = new Scanner(System.in);

		int noCases = sc.nextInt();
		int noElevations;
		int toAppend;
		String outputStr = "";

		// take in input and store inside elevationsArr
		for(int i = 0; i < noCases; i++) {
			noElevations = sc.nextInt() + 1;
			int[] elevationsArr = new int[noElevations];
			for(int j = 0; j < noElevations; j++) {
				elevationsArr[j] = sc.nextInt();
			}
			toAppend = findNoPostings(elevationsArr);
			outputStr += "Case #" + (i+1) + ": " + toAppend + "\n";
		}

		return outputStr;
	}

	// finds the maximum number of postings given an array of elevations
	static int findNoPostings(int[] elevationsArr) {
		Stack<Integer> gradients = new Stack<Integer>();
		int sizeArr = elevationsArr.length;
		int noValidSeparations = 0;
		int toPush;

		// add one to the no of valid separations if the gradient changes
		for(int i = 0; i < sizeArr - 1; i++) {
			if(elevationsArr[i] < elevationsArr [i + 1]) {
				toPush = 1;
			} else if(elevationsArr[i] > elevationsArr[i + 1]) {
				toPush = -1;
			} else {
				toPush = 0;
			}

			if(gradients.empty()) {
				if(toPush != 0) {
					gradients.push(toPush);
				}
			} else {
				if(!(gradients.peek()).equals(toPush) && (toPush != 0)) {
					gradients.pop();
					noValidSeparations++;
				}
			}
		}

		// maximum no of postings is the number of valid regions subtracted by 1
		return noValidSeparations - 1;
	}
}
