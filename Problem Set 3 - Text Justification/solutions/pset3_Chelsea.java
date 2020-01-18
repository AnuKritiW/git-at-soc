import java.util.*;

public class pset3_Chelsea {
    public static String[] justify(String[] words, int maxWidth) {
        int pointer = 0;
        int startLineFrom = 0;
        int charCount = 0;
        ArrayList<String> result = new ArrayList<>();
        
        while (pointer < words.length) {
            charCount += words[pointer].length();

            if (charCount > maxWidth) {
                // Overshot maxWidth, generate text for the words before
                result.add(pset3_Chelsea.padText(
                    Arrays.copyOfRange(words, startLineFrom, pointer), 
                    maxWidth,
                    false)
                );
                charCount = 0;
                startLineFrom = pointer;
            } else {
                charCount++; // add a space after each word
                pointer++;
            }
        }
        // Last line of words
        result.add(pset3_Chelsea.padText(
            Arrays.copyOfRange(words, startLineFrom, pointer), 
            maxWidth,
            true)
        );

        return result.toArray(new String[0]);
    }

    // Pads one line of text with necessary spaces
    private static String padText(String[] words, int maxWidth, boolean isLeftJustify) {
        String result = "";

        if (isLeftJustify || words.length == 1) {
            // Special case for last line or single word, left justify
            result += String.join(" ", words);
            result += nSpace(maxWidth - result.length());
            
            return result;
        }

        int numChars = Arrays.stream(words).mapToInt(x -> x.length()).sum();
        int numSpaces = maxWidth - numChars;
        int spaceLength = numSpaces / (words.length - 1);

        for (int i = 0; i < words.length - 1; i++) {
            result += words[i];
            result += nSpace(spaceLength);
            numSpaces -= spaceLength;
        }
        result += nSpace(numSpaces);
        result += words[words.length - 1];

        return result;
    }

    private static String nSpace(int n) {
        char[] spaces = new char[n];
        Arrays.fill(spaces, ' ');
        return new String(spaces);
    }

    public static void main(String[] args) {
        // String[] words = {"This", "is", "an", "example", "of", "text", "justification."};
        // String[] words = {"What","must","be","acknowledgment","shall","be"};
        String[] words = {"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"};
        int maxWidth = 20;
        String[] result = pset3_Chelsea.justify(words, maxWidth);

        System.out.println(Arrays.toString(result));
    }
}

