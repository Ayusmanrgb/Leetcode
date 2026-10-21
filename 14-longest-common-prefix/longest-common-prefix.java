class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        
        // Iterate through the characters of the first string
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            // Check this character against all other strings
            for (int j = 1; j < strs.length; j++) {
                // If the index exceeds the string length or characters don't match
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
