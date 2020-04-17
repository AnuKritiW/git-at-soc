class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true; //set 0th index to true as null is present in dict
        
        Set<String> wordSet = new HashSet(wordDict);
        
        for (int i = 1; i <= s.length(); i++) { //i is the last index of the first substring
            for (int j = 0; j < i; j++) { //j is the fist index of the first substring
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true; //set the index matching with the last char of substring to true
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
}

public class MainClass {
    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }
    
    public static String[] stringToStringArray(String line) {
        JsonArray jsonArray = JsonArray.readFrom(line);
        String[] arr = new String[jsonArray.size()];
        for (int i = 0; i < arr.length; i++) {
          arr[i] = jsonArray.get(i).asString();
        }
        return arr;
    }
    
    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);
            line = in.readLine();
            List<String> wordDict = stringToStringList(line);
            
            boolean ret = new Solution().wordBreak(s, wordDict);
            
            String out = booleanToString(ret);
            
            System.out.print(out);
        }
    }
}